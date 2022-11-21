from django.urls import path

from . import views

app_name = "providers"

urlpatterns = [
    path("create", views.ProviderCreateView.as_view(), name="provider-create"),
    path(
        "address/update/<int:id>/<int:pk>/",
        views.AddressUpdateView.as_view(),
        name="provider-address-update",
    ),
]
