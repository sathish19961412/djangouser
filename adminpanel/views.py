from django.shortcuts import render

# Create your views here.

def home(reqest):
    return render(reqest,"home.html")

def login(reqest):
    return render(reqest,"login.html")

def register(reqest):
    return render(reqest,"register.html")

