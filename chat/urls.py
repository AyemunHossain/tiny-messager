from django.urls import path, include
from .views import *


app_name = "chat"

urlpatterns = [
    path("", chat)
]
