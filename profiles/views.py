from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name  = 'common/home.html'

class Categories(TemplateView):
    template_name  = 'common/categories.html'

class CartPage(TemplateView):
    template_name  = 'common/carts.html'

    
class ContactPage(TemplateView):
    template_name  = 'common/contacts.html'

class CheckOutPage(TemplateView):
    template_name  = 'common/checkout.html'
    
class LoginPage(TemplateView):
    template_name  = 'common/login.html'

    

