from django import forms
from .models import ShortingUrls

# We are creating the form refers to our model.
# Go to views.py

class UrlsForm(forms.ModelForm):
    class Meta:
        model = ShortingUrls
        fields = ['normalUrl']