from django.urls import path
from .views import (
    CustomerListView, 
    CustomerCreateView, 
    CustomerUpdateView, 
    CustomerDeleteView
)
from django.contrib.auth.decorators import login_required

app_name = "customer"
urlpatterns = [
    path("list/", login_required(CustomerListView.as_view()), name="customer-list"),
    path("", CustomerCreateView.as_view(), name="customer-create"),
    path("<int:id>/", CustomerUpdateView.as_view(), name="customer-update"),
    path("<int:id>/delete/", CustomerDeleteView.as_view(), name="customer-delete"),
]
