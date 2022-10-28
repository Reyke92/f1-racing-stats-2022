from f1site.models import Driver, Event, GP, Team, Track

def getRankings(gp):
    rankings = {} # Rankings stored as { driver_id, points }.
    for event in gp.events:
        if rankings[event.driver_id] is None:
            rankings[event.driver_id] = 0

        rankings[event.driver_id] += event.qualPoints + event.racePoints
        if event.sprintPoints is not None:
            rankings[event.driver_id] += event.sprintPoints

    return sorted(rankings)
