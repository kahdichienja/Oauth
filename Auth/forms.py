from django.core.validators import validate_slug, validate_email
from django import forms

class ContactForm(forms.Form):
    name            = forms.CharField(label='Your name', max_length=100)
    email           = forms.EmailField(label='Your email')
    massege         = forms.CharField(widget = forms.Textarea())
    password        = forms.CharField(widget = forms.PasswordInput)

    # def clean_email(self):
    #       field level vaidation
    #     email_passed = self.cleaned_data.get("email")
    #     email_req    = "yourdomain.com"

    #     if not email_req in email_passed:
    #         raise forms.ValidationError("Invalid Email....")
    #     return email_passed    


    def clean(self):
        # form level validation
        cleaned_data = super(ContactForm, self).clean()
        # email validation
        email_passed = cleaned_data.get("email")
        email_req    = "gmail.com"
        if not email_req in email_passed:
            raise forms.ValidationError("Invalid Email....")
        # return email_passed 
        # password validation
        password_passed = cleaned_data.get("password")
        password_req    = "1234567890"

        if password_req == password_passed:
            raise forms.ValidationError("Fake password")
        return password_passed, email_passed 
        