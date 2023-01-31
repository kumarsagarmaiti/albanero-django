from django.urls import path
from . import views

urlpatterns = [
    path("register", views.create_employee),
    
]
