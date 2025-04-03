from django import forms
from django.contrib.auth.models import User
from .models import Order, IceCreamFlavor

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['flavor', 'quantity']

class FlavorForm(forms.ModelForm):
    class Meta:
        model = IceCreamFlavor
        fields = ['name']