from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.core.mail import BadHeaderError, EmailMessage
from django.conf import settings

# Create your views here.
class ContactIndex(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'contact/contact_index.html')

# TODOS: Refactor code - class based
def send(request):
    subject = request.POST.get('subject','')
    message = request.POST.get('message','')
    responder = request.POST.get('responder','')
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

        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return HttpResponseRedirect('/contact/thanks')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')

def thanks(request):
    return HttpResponse('ok')
