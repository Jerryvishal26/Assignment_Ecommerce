"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from profiles.views import Home
from profiles.views import Categories
from profiles.views import CartPage
from profiles.views import ContactPage
from profiles.views import CheckOutPage
from profiles.views import LoginPage
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(),name='home'),
    path('home.html/', Home.as_view(),name='home'),
    path('categories.html/', Categories.as_view(),name='categories'),
    path('carts.html/', CartPage.as_view(),name='carts'),
    path('contacts.html/', ContactPage.as_view(),name='contacts'),
    path('checkout.html/', CheckOutPage.as_view(),name='checkout'),
    path('checkout.html/home.html/', Home.as_view(),name='home'),
    path('login.html/', LoginPage.as_view(),name='login'),
    path('login.html/home.html/', Home.as_view(),name='home'),
    path('home.html/categories.html', Categories.as_view(),name='categories'),
    path('home.html/carts.html/', CartPage.as_view(),name='carts'),
    path('home.html/contacts.html/', ContactPage.as_view(),name='contacts'),
    path('home.html/login.html/', LoginPage.as_view(),name='login'),
    path('',TemplateView.as_view(template_name='index.html')),
   


]