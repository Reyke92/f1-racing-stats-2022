from datetime import datetime, timedelta
from os import path
from django.conf import settings
from django.core.paginator import Paginator
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from . import models


# URL: /
def viewIndex(request):
    context = {}
    return render(request, 'index.html', context)


# URL: /
def viewDriverRanking(request):
    context = {}
    return render(request, 'drivers.html', context)


# URL: /
def viewRaceRanking(request):
    context = {}
    return render(request, 'races.html', context)

    # URL: /


def viewTeamRanking(request):
    context = {}
    return render(request, 'teams.html', context)
