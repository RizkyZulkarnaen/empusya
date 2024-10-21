from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,  PasswordResetForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.admin.widgets import FilteredSelectMultiple

class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError("No user registered with this email address")
        return email