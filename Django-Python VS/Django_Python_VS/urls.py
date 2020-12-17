"""
Definition of urls for Django_Python_VS.
"""
from app import views
from app import forms, views

from datetime import datetime

from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('person/', views.Person, name='person'),
    path('view/', views.view, name='view'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('', views.view),
    path('create/', views.create),
]






