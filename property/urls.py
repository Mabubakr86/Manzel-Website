from django.urls import path
from .views import PropertyListView, PropertyDetailView


app_name = 'property'

urlpatterns = [
    path('', PropertyListView.as_view(), name='propert_list'),
    path('<slug:slug>/', PropertyDetailView.as_view(), name='propert_detail'),


]