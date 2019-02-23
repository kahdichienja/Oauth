from django.core.validators import validate_slug, validate_email
from django import forms
from datetime import datetime



# task form.
class TodoForm(forms.Form):
    name = forms.CharField(label='Todo name', max_length=100)
    Task = forms.CharField(label='Description', max_length=200,widget = forms.Textarea)
    # day = forms.DateField(initial=datetime.date.today)