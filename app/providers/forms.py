from django import forms
from django.forms import ModelForm

from .models import (Address, Contact, Education, ImmunisationStatement,
                     NextOfKin, OtherDetail, Provider, WorkInterest)


class ProviderCreateProfileForm(ModelForm):
    class Meta:
        model = Provider
        fields = ("provider",)
        widgets = {"provider": forms.HiddenInput()}


class AddressUpdateForm(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
        exclude = ("provider",)
        widgets = {"provider": forms.HiddenInput()}
        
        
class ContactUpdateForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("provider", 'tel1', 'tel2', 'email1')
        widgets = {"provider": forms.HiddenInput()}