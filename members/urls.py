from django.urls import path
from .views import UserRegisterView, logout_user
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
    
]