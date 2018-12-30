import sendgrid
from sendgrid.helpers.mail import Email, Content, Mail

from simple_personal_site.site_config import SENDGRID_APIKEY


class SendgridClient(object):
    def __init__(self, apikey):
        self.sg = sendgrid.SendGridAPIClient(apikey=apikey)

    # Send plaintext email with Sendgrid
    def send_plaintext(self, from_address, to_address, subject, text):
        from_email = Email(from_address)
        to_email = Email(to_address)
        content = Content('text/plain', text)
        mail = Mail(from_email, subject, to_email, content)
        response = self.sg.client.mail.send.post(request_body=mail.get())
        return response.status_code

    # Send HTML email with Sendgrid
    def send_html(self, from_address, to_address, subject, html):
        from_email = Email(from_address)
        to_email = Email(to_address)
        content = Content('text/html', html)
        mail = Mail(from_email, subject, to_email, content)
        response = self.sg.client.mail.send.post(request_body=mail.get())
        return response.status_code


if SENDGRID_APIKEY:
    sg_client = SendgridClient(SENDGRID_APIKEY)
else:
    sg_client = None
