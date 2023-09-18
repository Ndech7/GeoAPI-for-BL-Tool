from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.get_sites, name='api_home'),
]