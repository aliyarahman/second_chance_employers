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

def search(request):
    return render(request, "search.html")

def employer(employer, employer_id):
    return render(request, "employer.html")