from django.shortcuts import render
from django.views.generic.list import ListView
from .models import MyUser

# Create your views here.

class ProfileView(ListView):

    model = MyUser
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
