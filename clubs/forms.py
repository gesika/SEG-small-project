from django import forms
from django.forms import fields
from clubs.models import User
from django.core.validators import RegexValidator

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['username',]
        fields = ['first_name', 'last_name', 'email', 'bio', 'experience_level', 'personal_statement', 'user_type']
        widgets = {'bio': forms.Textarea(), 'personal_statement': forms.Textarea()}
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

    def save(self):
        """Create a new user."""

        super().save(commit=False)
        user = User.objects.create_user(
            self.cleaned_data.get('email'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            #email=self.cleaned_data.get('email'),
            bio=self.cleaned_data.get('bio'),
            experience_level=self.cleaned_data.get('experience_level'),
            user_type=self.cleaned_data.get('user_type'),
            personal_statement=self.cleaned_data.get('personal_statement'),
            password=self.cleaned_data.get('new_password'),
        )
        return user