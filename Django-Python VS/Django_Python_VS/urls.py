"""
Definition of urls for Django_Python_VS.
"""
from app import views
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('person/', views.Person, name='person'),
    path('about/', views.about, name='about'),
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
    # path('', views.Get_person, name='get_person'),
    # path('', views.Create_person, name='create_person'),
    path('', views.view),
    path('create/', views.create),
]






