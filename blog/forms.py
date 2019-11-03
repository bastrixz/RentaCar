from django import forms
from .models import Auto

class AutoForm(forms.ModelForm):

    class Meta:
        model = Auto
        fields = ('modelo', 'anio','color','marca','stock','imagen',)