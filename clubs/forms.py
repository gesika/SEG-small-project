from django import forms
from django.forms import fields
from clubs.models import Member
from django.core.validators import RegexValidator


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'username', 'email', 'bio', 'experience_level', 'personal_statement']
        widgets = {'bio': forms.Textarea(), 'personal_statement': forms.Textarea(), 'experience_level':forms.NumberInput()}
    new_password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        validators=[RegexValidator(
            regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
            message='Password must contain an uppercase character, a lowercase '
                    'character and a number'
            )]
    )
    password_confirmation = forms.CharField(label='Password confirmation', widget=forms.PasswordInput())
    
    def clean(self):
        """Clean the data and generate messages for any errors."""

        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'Confirmation does not match password.')
