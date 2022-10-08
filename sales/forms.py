from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import sale

User = get_user_model()

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



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}


