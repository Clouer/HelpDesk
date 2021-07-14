from django import forms

from helpdesk.models import User, Request


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class CreateRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'description', 'owner']
