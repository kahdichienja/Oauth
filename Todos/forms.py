from django.core.validators import validate_slug, validate_email
from django import forms
from django.forms.widgets import MultiWidget
from datetime import datetime



# task form.
class TodoForm(forms.Form):
    name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Task Name', 'class': 'validate', 'id': 'name', 'required': "true"}))
    Task = forms.CharField(max_length = 200, widget = forms.Textarea(attrs={'placeholder': 'Description...','class': 'materialize-textarea', 'id': 'task', 'required': "true"}))
    

    # school_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Name of School'),'class': 'form-control', 'id': 'school_name', 'data-parsley-required': "true", 'data-parsley-group': 'group0'}))