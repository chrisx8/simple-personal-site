from django.conf import settings
from django.core.mail import send_mail
from django.http import Http404, HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from global_config.site_config import SITE_NAME
from .forms import ContactForm
from .models import ContactConfig, Message


# message form
def message(request):
    try:
        contact_config = ContactConfig.objects.get()
        from_addr = f'{contact_config.from_name} <{contact_config.from_email}>'
        has_pgp_pubkey = bool(contact_config.pgp_pubkey)
    except ContactConfig.DoesNotExist:
        contact_config = None
        has_pgp_pubkey = False

    # check if configs for sending emails exist
    def can_email():
        smtp_configured = settings.EMAIL_HOST and settings.EMAIL_PORT and \
                          settings.EMAIL_HOST_USER and settings.EMAIL_HOST_PASSWORD
        contact_configured = contact_config and contact_config.from_name and contact_config.from_email
        return smtp_configured and contact_configured

    def email_site_owner():
        # check prereqs for emailing site owner
        if not can_email() or not contact_config.site_owner_email:
            return
        # build html email content
        mail_context = {'msg': new_msg}
        mail_html = render(request, 'notification_email.html', context=mail_context).content.decode("utf-8")
        # build text email content
        mail_text = render(request, 'notification_email.txt', context=mail_context).content.decode("utf-8")
        # send email to form submitter
        notification_subj = 'New message from %s' % new_msg.name
        send_mail(notification_subj, mail_text, from_addr,
                  [contact_config.site_owner_email], html_message=mail_html, fail_silently=True)

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
        send_mail(contact_config.subject, mail_text, from_addr,
                  [new_msg.email], html_message=mail_html, fail_silently=True)

    if request.method == 'POST':
        # get form data from post
        form = ContactForm(request.POST)
        # check honeypot
        if form.is_valid():
            form_data = form.cleaned_data
            if form_data['url']:
                return HttpResponse(status=400)
            # create message object
            new_msg = Message(name=form_data['name'], email=form_data['email'], message=form_data['message'])
            new_msg.save()
            # send emails
            email_sender()
            email_site_owner()
            return HttpResponseRedirect(reverse('message_success'))
        else:
            context = {'form': form, 'has_pgp': has_pgp_pubkey}
            return render(request, 'contact.html', context=context)
    else:
        context = {'form': ContactForm(), 'has_pgp': has_pgp_pubkey}
        return render(request, 'contact.html', context=context)


# thank-you page
def message_success(request):
    return render(request, 'message_success.html')


# pgp pubkey
def show_pgp_pubkey(request):
    # check if key exists
    try:
        contact_config = ContactConfig.objects.get()
        pgp_pubkey = str(contact_config.pgp_pubkey)
        assert len(pgp_pubkey) > 0
        return HttpResponse(pgp_pubkey, content_type='text/plain')
    except (AssertionError, ContactConfig.DoesNotExist):
        raise Http404
