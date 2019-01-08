from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView
from .forms import ContactForm

# Create your views here.
class ContactIndex(FormView):
    template_name = 'contact/contact_index.html'
    form_class = ContactForm
    success_url = '/contact/thanks'

    def form_valid(self, form):
        form.send_email()
        return super(ContactIndex, self).form_valid(form)

class ContactSuccess(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'contact/contact_success.html')
