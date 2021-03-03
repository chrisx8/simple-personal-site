import requests
from bleach import clean
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render, HttpResponse, Http404
from django.template.loader import render_to_string
from .forms import ContactForm
from .models import ContactConfig, Message


# message form and contact info
def contact(request):
    # get config`
    contact_config = ContactConfig.objects.get_or_create()[0]
    pgp_fingerprint = contact_config.pgp_fingerprint
    has_pgp_key = bool(contact_config.pgp_key)
    hcaptcha_sitekey = contact_config.hcaptcha_site_key
    hcaptcha_secret = contact_config.hcaptcha_secret_key
    hcaptcha_fail = False

    # check if configs for sending emails exist
    def can_email():
        smtp_configured = settings.EMAIL_HOST and settings.EMAIL_PORT and \
                          settings.EMAIL_HOST_USER and settings.EMAIL_HOST_PASSWORD
        contact_configured = contact_config and contact_config.from_email
        return smtp_configured and contact_configured

    def send_notification_email():
        # check prereqs for emailing site owner
        if not can_email() or not contact_config.notification_recipient:
            return
        # build text email content
        mail_context = {'msg': new_msg}
        mail_text = render_to_string('notification_email.txt', context=mail_context)
        # send email to notification recipient
        from_addr = f"{new_msg.name} - {new_msg.email.replace('@', '{at}')} <{contact_config.from_email}>"
        email = EmailMessage(f'[Contact Form] {new_msg.subject}', mail_text, from_addr,
                             [contact_config.notification_recipient], reply_to=[new_msg.email])
        email.send(fail_silently=True)

    def hcaptcha_validate(response):
        # pass check if not configured
        if not hcaptcha_sitekey:
            return True
        # validate captcha with API
        hcaptcha_req = requests.post('https://hcaptcha.com/siteverify',
                                     data={'secret': hcaptcha_secret, 'response': response})
        # check for success
        return hcaptcha_req.json()['success']

    if request.method == 'POST':
        # get form data from post
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                # get captcha response
                hcaptcha_resp = form.data['h-captcha-response']
            except KeyError:
                hcaptcha_resp = ''
            # captcha validation
            is_human = hcaptcha_validate(hcaptcha_resp)
            if is_human:
                data = form.cleaned_data
                # save message
                new_msg = Message(name=data['name'], email=data['email'], 
                                  subject=data['subject'], message=data['message'])
                new_msg.save()
                # send notification, fail silently
                send_notification_email()
                return render(request, 'contact_success.html')
            # failed captcha
            hcaptcha_fail = True
    else:
        form = ContactForm()

    # render form
    context = {
        'form': form,
        'hcaptcha_fail': hcaptcha_fail,
        'hcaptcha_sitekey': hcaptcha_sitekey,
        'pgp_fingerprint': pgp_fingerprint,
        'has_pgp_key': has_pgp_key
    }
    return render(request, 'contact.html', context=context)


def pgp_key(request):
    contact_config = ContactConfig.objects.get_or_create()[0]
    pgp_key = contact_config.pgp_key
    # 404 if key isn't configured
    if not pgp_key:
        raise Http404
    return HttpResponse(pgp_key, content_type='text/plain')
