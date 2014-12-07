from django.shortcuts import render

import urlparse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def rate(request):
    return render(request, "rate.html")

def search(request):
    return render(request, "search.html")

def results(request):
    employers = Employer.objects.all()
    return render(request, "results.html", {'employers':employers})

def employer_home(employer):
    return render(request, "employer_home.html")

def add_employer(employer, employer_id):
    return render(request, "add_employer.html")

def edit_employer(employer, employer_id):
    return render(request, "edit_employer.html")