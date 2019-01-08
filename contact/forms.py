from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, EmailMessage
from django.conf import settings

class ContactForm(forms.Form):
    subject = forms.CharField()
    responder = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        subject = self.cleaned_data['subject']
        responder = self.cleaned_data['responder']
        message = self.cleaned_data['message']

        if subject and message and responder:
            try:

                # Initial fields
                email = EmailMessage(
                    subject,
                    message,
                    responder,
                    [settings.EMAIL_ADMIN],
                    reply_to=[responder],
                )

                # Send email
                email.send()

                pass
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponseRedirect('/contact/thanks')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    