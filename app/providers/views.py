from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from users.models import User

from .forms import AddressUpdateForm, ProviderCreateProfileForm
from .models import Address, Provider


class ProviderCreateView(CreateView):
    model = Provider
    form_class = ProviderCreateProfileForm

    def get_initial(self):
        # Get the initial dictionary from the superclass method
        initial = super(ProviderCreateView, self).get_initial()
        # Copy the dictionary so we don't accidentally change a mutable dict
        initial = initial.copy()
        # provider = User.objects.get(pk=2)
        # initial['provider'] = provider
        initial["provider"] = self.request.user
        print(initial["provider"])
        # etc...
        return initial

    def form_valid(self, form):
        # provider = User.objects.get(pk=2)
        form.instance.provider = self.request.user
        form.save()
        return super(ProviderCreateView, self).form_valid(form)


class AddressUpdateView(UpdateView):
    model = Address
    form_class = AddressUpdateForm
