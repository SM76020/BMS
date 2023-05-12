from django import forms
from .models import Accholder

class bank(forms.ModelForm):
    class Meta:
        model=Accholder
        fields="__all__"