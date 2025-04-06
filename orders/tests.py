#from django.test import TestCase

import pytest
from django.contrib.auth.models import User
from .models import IceCreamFlavor, Order

@pytest.mark.django_db
def test_icecream_flavor_str():
    flavor = IceCreamFlavor.objects.create(name="Chocolate")
    assert str(flavor) == "Chocolate"

@pytest.mark.django_db
def test_order_str():
    user = User.objects.create_user(username='testuser', password='12345')
    flavor = IceCreamFlavor.objects.create(name="Vanilla")
    order = Order.objects.create(user=user, flavor=flavor, quantity=2)
    assert str(order) == "testuser ordered 2 of Vanilla"
    


from django.urls import reverse, resolve
from . import views

def test_index_url():
    assert reverse('index') == '/'
    assert resolve('/').func == views.index

def test_signup_url():
    assert reverse('signup') == '/signup/'
    assert resolve('/signup/').func == views.signup_view

def test_order_create_url():
    assert reverse('order_create') == '/orders/create/'
    assert resolve('/orders/create/').func == views.order_create

# Add more as needed






# Create your tests here
