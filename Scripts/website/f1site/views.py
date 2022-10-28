from datetime import datetime, timedelta
from os import path
from django.conf import settings
from django.core.paginator import Paginator
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from f1site.models import Driver, Event, GP, Team, Track
from .f1utils import getRankings


# URL: /
def viewIndex(request):
    context = {}
    return render(request, 'index.html', context)


# URL: /drivers
def viewDriverRanking(request):
    gp = GP.objects.filter(date__year=datetime.now().year.real)

    context = {'drivers': Driver.objects.all()}
    return render(request, 'drivers.html', context)


# URL: /races
def viewRaces(request):
    context = {'gpArray': GP.objects.all()}
    return render(request, 'races.html', context)


# URL: /races/<gpID>
def viewRaceRanking(request, gpID):
    gp = get_object_or_404(GP, id=gpID)
    context = {'gp': gp}
    return render(request, 'races.html', context)


# URL: /teams
def viewTeamRanking(request):
    context = {}
    return render(request, 'teams.html', context)
