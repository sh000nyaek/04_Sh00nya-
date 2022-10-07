from django import forms
from .models import sale


class SaleModelForm(forms.ModelForm):
    class Meta:
        model = sale
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent', 
        )




class SaleForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)