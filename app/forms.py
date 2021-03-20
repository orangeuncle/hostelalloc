from django.db import models
from django.forms import ModelForm
from django import forms


# SEX_CHOICES = [
#     ('Male','Male'),
#     ('Female','Female')
# ]
PAYMENT_CHOICES = [
    ('Tuition','Tuition'),
    ('Full','Full')
]

class PaymentForm(forms.Form):
    name = forms.CharField(max_length=100)
    regNo = forms.CharField(max_length=15)
    # sex = forms.ChoiceField(widget=forms.RadioSelect, choices=SEX_CHOICES)
    Payment = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class SearchForm(forms.Form):
    regNo = forms.CharField(max_length=15)

class HostelSearchForm(forms.Form):
    Hostel_Name = forms.CharField(max_length=100)


