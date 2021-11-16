from django import forms
from django.forms import fields
from clubs.models import Member


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'username', 'email', 'bio', 'experience_level', 'personal_statement']
        widgets = {'bio': forms.Textarea(), 'personal_statement': forms.Textarea(), 'experience_level':forms.NumberInput()}
    new_password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput())