from django.urls import path
from . import views
from .Auth import views as views_auth

urlpatterns = [
	path('', views.index, name='index'),
	path('register/', views_auth.register, name='register'),
]