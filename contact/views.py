from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.core.mail import BadHeaderError, send_mail

# Create your views here.
class ContactIndex(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'contact/contact_index.html')

# TODOS: Refactor code - class based
def send(request):
    subject = request.POST.get('subject','')
    message = request.POST.get('message','')
    responser = request.POST.get('responder','')
    if subject and message and responser:
        try:
            send_mail(subject, message, responser, ['yourEmail@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return HttpResponseRedirect('/contact/thanks')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')

def thanks(request):
    return HttpResponse('ok')
