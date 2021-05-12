from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .support.fetch_data import fetch_data

# Create your views here.


def reports(request):
    stats = {
        "table": fetch_data()
    }
    return render(request, "reports/home.html", stats)
