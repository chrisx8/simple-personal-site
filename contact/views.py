from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from simple_personal_site.sendgrid import sg_client
from simple_personal_site.site_config import CONTACT_EMAIL
from .forms import ContactForm
from .models import Message, SocialMediaLink


# contact page
def contact(request):
    # get social media links
    social_links = SocialMediaLink.objects.filter(show=True).order_by('platform')
    context = {'social_links': social_links}
    return render(request, 'contact.html', context=context)


# message form
def message(request):
    if request.method == 'POST':
        # get form data from post
        form = ContactForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            # create message object
            new_msg = Message(name=form_data['name'], email=form_data['email'], message=form_data['message'])
            new_msg.save()
            if sg_client:
                # render email content
                mail_context = {
                    'name': new_msg.name,
                    'msg': new_msg.message
                }
                mail_content = render(request, 'message_email.html', context=mail_context).content.decode("utf-8")
                # send email
                sg_client.send_html(CONTACT_EMAIL['from'], new_msg.email, CONTACT_EMAIL['subject'], mail_content)
            return HttpResponseRedirect(reverse('message_success'))
        else:
            context = {'form': form}
            return render(request, 'message.html', context=context)
    else:
        context = {'form': ContactForm()}
        return render(request, 'message.html', context=context)


# thank-you page
def message_success(request):
    return render(request, 'message_success.html')
