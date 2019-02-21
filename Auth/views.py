from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm


# Create your views here.

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'Auth/form/form.html'
    success_url = '/'