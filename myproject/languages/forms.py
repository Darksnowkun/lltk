from django.forms import ModelForm
from .models import languages

class EditLanguageForm(ModelForm):
    class Meta:
        model = languages
        fields = ['language']

