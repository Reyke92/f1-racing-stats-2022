from datetime import datetime, timedelta
from os import path
from django.conf import settings
from django.core.paginator import Paginator
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from f1site.models import Driver, Event, GP, Team, Track, Qualifying, Sprint, Race
from .f1utils import getYearRankings, getRankingsByPosition, getRankingsByPoints


# URL: /
def viewIndex(request):
    curYear = datetime.now().year
    rankings = getYearRankings(curYear)

    context = {
        'currentYear': curYear,
        'rankings' : rankings
    }
    return render(request, 'index.html', context)


# URL: /drivers
def viewDriverRanking(request):
    gp = GP.objects.filter(date__year=datetime.now().year.real)

    context = {'drivers': Driver.objects.all()}
    return render(request, 'drivers.html', context)


# URL: /races
def viewRaces(request):
    context = {'gpArray': GP.objects.all()}
    return render(request, 'gp.html', context)


# URL: /gp/<gpID>
def viewGPRanking(request, gpID):
    gp = get_object_or_404(GP, id=gpID)
    rankings = getRankingsByPosition(gp)
    context = {
        'gp': gp,
        'raceRankings': rankings['raceRankings'],
        'qualRankings': rankings['qualRankings'],
        'NON_SPRINT': GP.GPType.NON_SPRINT,
        'SPRINT': GP.GPType.SPRINT
    }
    for ranking in context['raceRankings']:
        ranking.driver = Driver.objects.get(id=ranking.driverID)
    for ranking in context['qualRankings']:
        ranking.driver = Driver.objects.get(id=ranking.driverID)

    if ('sprintRankings' in rankings):
        context['sprintRankings'] = rankings['sprintRankings']
        for ranking in context['sprintRankings']:
            ranking.driver = Driver.objects.get(id=ranking.driverID)

    return render(request, 'gp.html', context)


# URL: /teams
def viewTeamRanking(request):
    context = {}
    return render(request, 'teams.html', context)
