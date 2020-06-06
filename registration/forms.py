from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    # It has to be clean_fieldname. If other word is used, it won't work.
    # Validating that the email is unique
    def clean_email(self):
        # Get the email that has been sent by the form
        email = self.cleaned_data.get("email")
        # Check if the email exists already
        if User.objects.filter(email=email).exists():
            # IF exists, raise error
            raise forms.ValidationError("El email ya está registrado. Prueba con otro.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt3'}),
            'bio': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Biografía'}),
            'link': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Enlace'}),
        }