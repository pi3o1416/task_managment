
from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .models import User


class UserForm(forms.ModelForm):
    MIN_AGE = 5
    error_messages = {
        'under_age': _('Age can not be less than {}'.format(MIN_AGE))
    }
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label=_('Date Of Birth'),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth', 'first_name', 'last_name']

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            if self.is_date_of_birth_invalid(date_of_birth):
                raise forms.ValidationError(
                    message=self.error_messages['under_age'],
                    code='under_age',
                )
        return date_of_birth

    @staticmethod
    def get_user_age(date_of_birth):
        today = timezone.localdate()
        age = (today - date_of_birth).days // 365
        return age

    def is_date_of_birth_invalid(self, date_of_birth):
        age = self.get_user_age(date_of_birth)
        return True if age < self.MIN_AGE or age < 0 else False


class UserCreateForm(UserForm):
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
        'under_age': _('User should be at least 15 years old'),
        'duplicate_username': _('Username already exist'),
        'duplicate_email': _('Email already exist'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
