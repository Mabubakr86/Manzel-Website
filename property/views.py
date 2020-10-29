from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class PropertyListView(ListView):
    model = Property

class PropertyDetailView(DetailView):
    model = Property

    def get_context_data(self,*args,**kwargs):
        context = super(PropertyDetailView, self).get_context_data(*args,**kwargs)
        prop_filter = Property.objects.filter(location=self.get_object().location)
        # if prop_filter.count > 1:
        context['related'] = prop_filter 
        # need to handle less than 3 logic                             
        return context
