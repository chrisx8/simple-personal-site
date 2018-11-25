from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from sg_client.sendgrid import sg_client
from .forms import ContactForm
from .models import Message
from simple_personal_site.site_config import CONTACT_EMAIL

def contact(request):
    if request.method == 'POST':
        # get form data from post
        form = ContactForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            # create message object
            new_msg = Message(name=form_data['name'], email=form_data['email'], message=form_data['message'])
            new_msg.save()
            # render email content
            mail_context = {
                'name': new_msg.name,
                'msg': new_msg.message
            }
            mail_content = render(request, 'contact_email.html', context=mail_context).content.decode("utf-8")
            # send email
            sg_client.send_html(CONTACT_EMAIL['from'], new_msg.email, CONTACT_EMAIL['subject'], mail_content)
        return HttpResponseRedirect(reverse('contact_success'))
    else:
        context = {'form': ContactForm()}
        return render(request, 'contact.html', context=context)


def success(request):
    return render(request, 'contact_success.html')