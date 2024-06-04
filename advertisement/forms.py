from django import forms
from .models import *


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'about', 'price', 'img']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'})
        }
