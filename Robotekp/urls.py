"""Robotekp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""



from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url, handler404
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import logout_then_login
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='Tienda/login.html'), name="login"),
    path('logout',logout_then_login,name='logout'),
    path('index/',include ('Tienda.urls',namespace=None)),
    path('accounts/',include('django.contrib.auth.urls')),
]
