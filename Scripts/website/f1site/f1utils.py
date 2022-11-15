from f1site.models import Driver, Event, GP, Team, Track, Qualifying, Sprint, Race


class Ranking():
    def __init__(self, driverID, points):
        self.driverID = driverID
        self.points = points


# Returns the winners of each of the GPs within the year specified.
def getYearRankings(year):
    rankings = []
    gps = GP.objects.filter(date__year=year)
    for gp in gps:
        ranking = getRankings(gp)[0]
        ranking.gp = gp
        ranking.driver = Driver.objects.get(id=ranking.driverID)
        rankings.append(ranking)

    return rankings


# Rankings are stored in the format of key-value:
# Key = driverID
# Value = Ranking
# sorted from greatest to least.
def getRankings(gp):
    # Rankings are stored as rankings[driver_id] = Ranking
    rankings = {}
    events = Event.objects.filter(gp_id=gp.id)
    pointsToAdd = 0
    for event in events:
        pointsToAdd = 0
        if (event.driver_id not in rankings):
            rankings[event.driver_id] = Ranking(driverID=event.driver_id, points=0)

        pointsToAdd += event.race.points
        if (event.type is event.EventType.SPRINT):
            pointsToAdd += event.sprint.points
            
        rankings[event.driver_id].points += pointsToAdd

    # Convert the dictionary to a list
    rankingsArray = [None] * len(rankings)
    i = 0
    for rankingKey in rankings:
        rankingsArray[i] = rankings[rankingKey]
        i += 1

    # Sort the rankings array in order of greatest to least points.
    numRankings = len(rankingsArray)
    curPoints = 0
    curGreatestNum = -1
    curGreatestNumIndex = 0
    i = 0
    while (i < numRankings - 1):
        curPoints = rankingsArray[i].points
        k = i + 1
        while (k < numRankings):
            if (rankingsArray[k].points > curGreatestNum):
                curGreatestNum = rankingsArray[k].points
                curGreatestNumIndex = k
            k += 1 # Increment k.

        if (curPoints < curGreatestNum):
            tmp = rankingsArray[i]
            rankingsArray[i] = rankingsArray[curGreatestNumIndex]
            rankingsArray[curGreatestNumIndex] = tmp
        i += 1 # Increment i.
    return rankingsArray
