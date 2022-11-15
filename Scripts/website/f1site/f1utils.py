from f1site.models import Driver, Event, GP, Team, Track, Qualifying, Sprint, Race

MAX_NUM_RACERS = 35
ELEM_IDX_DRIVER_ID = 0
ELEM_IDX_POINTS = 1


def getYearRankings(year):
    rankings = []
    gps = GP.objects.filter(date__year=year)
    for gp in gps:
        rankings.append(getRankings(gp)[0])

    return rankings


def getRankings(gp):
    # Rankings are stored as rankings[_hashDriverID(driver_id)] = [driver_id, points].
    rankings = [None] * MAX_NUM_RACERS
    events = Event.objects.filter(gp_id=gp.id)
    for event in events:
        hashID = _hashDriverID(event.driver_id)
        if rankings[hashID] is None:
            rankings[hashID] = [event.driver_id, 0] # driverID, points

        race = Race.objects.get(event_id=event.id)
        rankings[hashID][ELEM_IDX_POINTS] += race.points

    # Remove any and all null keys in the rankings array.
    rankIndex = 0
    for ranking in rankings:
        if ranking is None:
            del rankings[rankIndex]
        else:
            rankIndex += 1

    # TODO: SORT THIS YOURSELF! MAYBE USING BUBBLE SORT...
    #return sorted(rankings)


def _hashDriverID(id):
    return id % MAX_NUM_RACERS # Estimated max upper-limit of the number of racers total.
