
from django import forms
from .models import Kayit

class KayitForm(forms.ModelForm):
    class Meta:
        model = Kayit
        fields = ['ad', 'soyad', 'email']
