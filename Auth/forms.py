from django.core.validators import validate_slug, validate_email
from django import forms

class ContactForm(forms.Form):
    name            = forms.CharField(label='Your name', max_length=100)
    validate_email  = forms.EmailField(label='Your email')
    content         = forms.CharField(widget = forms.Textarea())