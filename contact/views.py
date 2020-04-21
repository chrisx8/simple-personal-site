import requests
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.forms.utils import ValidationError
from django.shortcuts import render
from django.urls import reverse
from .forms import ContactForm
from .models import ContactConfig, Message


# message form and contact info
def contact(request):
    # get config`
    contact_config = ContactConfig.objects.get_or_create()[0]
    from_addr = f'{contact_config.from_name} <{contact_config.from_email}>'
    pgp_fingerprint = contact_config.pgp_fingerprint
    pgp_url = contact_config.pgp_url
    hcaptcha_sitekey = contact_config.hcaptcha_site_key
    hcaptcha_secret = contact_config.hcaptcha_secret_key
    hcaptcha_fail = False

    # check if configs for sending emails exist
    def can_email():
        smtp_configured = settings.EMAIL_HOST and settings.EMAIL_PORT and \
                          settings.EMAIL_HOST_USER and settings.EMAIL_HOST_PASSWORD
        contact_configured = contact_config and contact_config.from_name and contact_config.from_email
        return smtp_configured and contact_configured

    def email_site_owner(msg_sender):
        # check prereqs for emailing site owner
        if not can_email() or not contact_config.site_owner_email:
            return
        # build html email content
        mail_context = {'msg': new_msg}
        mail_html = render(request, 'notification_email.html', context=mail_context).content.decode("utf-8")
        # build text email content
        mail_text = render(request, 'notification_email.txt', context=mail_context).content.decode("utf-8")
        # send email to site owner
        email = EmailMultiAlternatives('Message from %s' % new_msg.name, mail_text, from_addr,
                                       [contact_config.site_owner_email], reply_to=[msg_sender])
        email.attach_alternative(mail_html, "text/html")
        email.send(fail_silently=True)

    def email_sender():
        # check prereqs for emailing sender
        if not can_email() or not contact_config.subject:
            return
        # build html email content
        mail_context = {'msg': new_msg}
        mail_html = render(request, 'message_email.html', context=mail_context).content.decode("utf-8")
        # build text email content
        mail_text = render(request, 'message_email.txt', context=mail_context).content.decode("utf-8")
        # send email to form submitter
        email = EmailMultiAlternatives(contact_config.subject, mail_text, from_addr, [new_msg.email])
        email.attach_alternative(mail_html, "text/html")
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
                new_msg = Message(name=data['name'], email=data['email'], message=data['message'])
                new_msg.save()
                # send emails
                email_sender()
                email_site_owner(data['email'])
                return render(request, 'contact_success.html')
            else:
                hcaptcha_fail = True
    else:
        form = ContactForm()

    # render form
    context = {
        'form': form,
        'hcaptcha_fail': hcaptcha_fail,
        'hcaptcha_sitekey': hcaptcha_sitekey,
        'pgp_fingerprint': pgp_fingerprint, 
        'pgp_url': pgp_url
    }
    return render(request, 'contact.html', context=context)
