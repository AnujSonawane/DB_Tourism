from django import forms
from .models import user1

class detailsform(forms.ModelForm):
    class Meta:
        model=user1
        fields="__all__"