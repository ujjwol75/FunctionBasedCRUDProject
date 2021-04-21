from django import forms
from .models import User
from django.core import validators

class StudentRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "email", "password"]
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'})

        }
        