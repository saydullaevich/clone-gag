from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from .models import User
from django.utils.translation import gettext_lazy as _



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label=_("Login"))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, label=_("Parol"))

class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(max_length=100, widget=forms.PasswordInput, label=_("Parol takroran"))

    def clean_confirm(self):
        if self.cleaned_data['confirm'] != self.cleaned_data['password']:
            raise ValidationError(_("Parollar bir xil emas"))
        return self.cleaned_data['confirm']
    
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': _("Login"),
            'password': _("Parol")
        }
        help_texts = {
            'username': _("Lotin harflari, sonlar va @/./+/-/_ belgilaridan iborat bo'lishi lozim.")
        }
        widgets = {
            'password': forms.PasswordInput
        }