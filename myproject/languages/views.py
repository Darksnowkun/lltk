from django.shortcuts import render
from languages.models import languages
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from .forms import EditLanguageForm

# Create your views here.

class ListOfLanguages(ListView):
    model = languages
    template_name = "listoflanguages.html"

class EditLanguages(CreateView):
    template_name = "editlanguages.html"
    form_class = EditLanguageForm
    success_url = "/"
