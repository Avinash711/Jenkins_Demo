
from django.urls import path
from .views import greet

urlpatterns = [
    path('jenkinsGreet/', greet),
]