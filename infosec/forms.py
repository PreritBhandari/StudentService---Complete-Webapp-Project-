from django import forms

# Creating ModelForm for Information Section

from .models import Information


class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['resume', 'phone_no', 'father_name', 'mother_name', 'address', 'guardian_no', 'github_link',
                  'facebook_link']
