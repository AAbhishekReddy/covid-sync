from typing import KeysView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reports, name = "reports-home"),
]