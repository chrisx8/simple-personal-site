from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from simple_personal_site.site_config import SITE_NAME
from .forms import ContactForm
from .models import ContactConfig, Message


# message form
def message(request):
    try:
        contact_config = ContactConfig.objects.get()
        from_addr = f'{contact_config.from_name} <{contact_config.from_email}>'
    except ContactConfig.DoesNotExist:
        contact_config = None

    def from_addr_exists():
        return contact_config.from_name and contact_config.from_email

    def site_owner_email_exists():
        return bool(contact_config.site_owner_email)

    def subject_exists():
        return bool(contact_config.subject)

    def email_site_owner():
        if not contact_config or not from_addr_exists() or not site_owner_email_exists():
            return
        # build html email content
        mail_context = {'msg': new_msg}
        mail_html = render(request, 'notification_email.html', context=mail_context).content.decode("utf-8")
        # build text email content
        mail_text = render(request, 'notification_email.txt', context=mail_context).content.decode("utf-8")
        # send email to form submitter
        notification_subj = '[%s] New message from %s' % (SITE_NAME, new_msg.name)
        send_mail(notification_subj, mail_text, from_addr,
                  [contact_config.site_owner_email], html_message=mail_html, fail_silently=True)

    def email_submitter():
        if not contact_config or not from_addr_exists() or not subject_exists():
            return
        # build html email content
        mail_context = {'name': new_msg.name, 'msg': new_msg.message}
        mail_html = render(request, 'message_email.html', context=mail_context).content.decode("utf-8")
        # build text email content
        mail_text = render(request, 'message_email.txt', context=mail_context).content.decode("utf-8")
        # send email to form submitter
        send_mail(contact_config.subject, mail_text, from_addr,
                  [new_msg.email], html_message=mail_html, fail_silently=True)

    if request.method == 'POST':
        # get form data from post
        form = ContactForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            # create message object
            new_msg = Message(name=form_data['name'], email=form_data['email'], message=form_data['message'])
            new_msg.save()
            # send emails
            email_submitter()
            # send email to site owner
            email_site_owner()
            return HttpResponseRedirect(reverse('message_success'))
        else:
            context = {'form': form}
            return render(request, 'contact.html', context=context)
    else:
        context = {'form': ContactForm()}
        return render(request, 'contact.html', context=context)


# thank-you page
def message_success(request):
    return render(request, 'message_success.html')
