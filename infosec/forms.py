from django import forms

# Creating ModelForm for Information Section
from .models import Information


class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['resume']
