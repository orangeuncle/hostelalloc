from django.db import models
from django.forms import ModelForm
from django import forms

SEX_CHOICES = [
    'Male',
    'Female'
]

class PaymentForm(forms.Form):
    name = forms.CharField(max_length=100)
    regNo = forms.CharField(max_length=12)
    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=SEX_CHOICES)
    Payment = forms.CharField(max_length=12)


