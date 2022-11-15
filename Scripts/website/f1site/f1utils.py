from f1site.models import Driver, Event, GP, Team, Track, Qualifying, Sprint, Race

MAX_NUM_RACERS = 35

class Ranking():
    def __init__(self, driverID, points):
        self.driverID = driverID
        self.points = points

    def computeHash(self):
        return _hashDriverID(self.driverID)

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


# Rankings are stored in the format of [driver_id, points], sorted from greatest to least.
def getRankings(gp):
    # Rankings are stored as rankings[_hashDriverID(driver_id)] = [driver_id, points].
    rankings = [None] * MAX_NUM_RACERS
    events = Event.objects.filter(gp_id=gp.id)
    for event in events:
        hashID = _hashDriverID(event.driver_id)
        if (rankings[hashID] is None):
            rankings[hashID] = Ranking(driverID=event.driver_id, points=0)

        rankings[hashID].points += event.race.points
        if (event.sprint is not None):
            rankings[hashID].points += event.sprint.points

    # Remove any and all null keys in the rankings array.
    rankIndex = 0
    numRankings = len(rankings)
    while (rankIndex < numRankings):
        ranking = rankings[rankIndex]
        if (ranking is None):
            rankings.pop(rankIndex)
            numRankings -= 1
        else:
            rankIndex += 1

    # Sort the rankings array in order of greatest to least points.
    numRankings = len(rankings)
    curPoints = 0
    curGreatestNum = -1
    curGreatestNumIndex = 0
    i = 0
    while (i < numRankings - 1):
        curPoints = rankings[i].points
        k = i + 1
        while (k < numRankings):
            if (rankings[k].points > curGreatestNum):
                curGreatestNum = rankings[k].points
                curGreatestNumIndex = k
            k += 1 # Increment k.

        if (curPoints < curGreatestNum):
            tmp = rankings[i]
            rankings[i] = rankings[curGreatestNumIndex]
            rankings[curGreatestNumIndex] = tmp
        i += 1 # Increment i.

    return rankings


def _hashDriverID(id):
    return id % MAX_NUM_RACERS # Estimated max upper-limit of the number of racers total.
