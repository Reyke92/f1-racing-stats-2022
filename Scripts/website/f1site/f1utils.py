from f1site.models import Driver, Event, GP, Team, Track, Qualifying, Sprint, Race


class Ranking():
    def __init__(self, driverID, points, position=None, totalTime=None):
        self.driverID = driverID
        self.points = points
        self.position = position
        self.totalTime = totalTime


# Returns the winners of each of the GPs within the year specified.
def getYearRankings(year):
    rankings = []
    gps = GP.objects.filter(date__year=year)
    for gp in gps:
        ranking = getRaceRankingsByPosition(gp)[0]
        ranking.gp = gp
        ranking.driver = Driver.objects.get(id=ranking.driverID)
        rankings.append(ranking)

    return rankings


# Rankings are stored in the format of key-value:
# Key = driverID
# Value = Ranking
# sorted from greatest to least IN TERMS OF POSITION.
def getRankingsByPosition(gp):
    # Rankings are stored as rankings[driver_id] = Ranking
    events = Event.objects.filter(gp_id=gp.id)

    raceRankings = getRaceRankingsByPosition(gp, events=events)
    qualRankings = getQualRankingsByPosition(gp, events=events)

    results = {
        'raceRankings': raceRankings,
        'qualRankings': qualRankings
    }
    if (gp.type == GP.GPType.SPRINT):
        results['sprintRankings'] = getSprintRankingsByPosition(gp, events=events)

    return results


def getRaceRankingsByPosition(gp, events=None):
    # Rankings are stored as rankings[driver_id] = Ranking
    rankings = {}
    if (events is None):
        events = Event.objects.filter(gp_id=gp.id)

    for event in events:
        if (event.driver_id not in rankings):
            rankings[event.driver_id] = Ranking(
                driverID=event.driver_id,
                points=0,
                position=event.race.position,
                totalTime=event.race.totalTime
            )

        rankings[event.driver_id].points += event.race.points

    # Convert the dictionary to a list
    rankingsArray = [None] * len(rankings)
    i = 0
    for rankingKey in rankings:
        rankingsArray[i] = rankings[rankingKey]
        i += 1

    # Sort the rankings array in order of greatest to least position.
    numRankings = len(rankingsArray)
    curPos = 0
    curGreatestPos = -1
    curGreatestPosIndex = 0
    i = 0
    while (i < numRankings - 1):
        curPos = rankingsArray[i].position
        k = i + 1
        while (k < numRankings):
            if (rankingsArray[k].position > curGreatestPos):
                curGreatestPos = rankingsArray[k].position
                curGreatestPosIndex = k
            k += 1  # Increment k.

        if (curPos < curGreatestPos):
            tmp = rankingsArray[i]
            rankingsArray[i] = rankingsArray[curGreatestPosIndex]
            rankingsArray[curGreatestPosIndex] = tmp
        i += 1  # Increment i.
    return rankingsArray


# Rankings are stored in the format of key-value:
# Key = driverID
# Value = Ranking
# sorted from greatest to least IN TERMS OF POINTS.
def getSprintRankingsByPosition(gp, events=None):
    if (gp.type == GP.GPType.NON_SPRINT): return None

    # Rankings are stored as rankings[driver_id] = Ranking
    rankings = {}
    if (events is None):
        events = Event.objects.filter(gp_id=gp.id)

    for event in events:
        if (event.sprint is not None): # Make sure that they have raced in a Sprint.
            if (event.driver_id not in rankings):
                rankings[event.driver_id] = Ranking(
                    driverID=event.driver_id,
                    points=0,
                    position=event.sprint.position,
                    totalTime=event.sprint.totalTime
                )

            rankings[event.driver_id].points += event.sprint.points

    # Convert the dictionary to a list
    rankingsArray = [None] * len(rankings)
    i = 0
    for rankingKey in rankings:
        rankingsArray[i] = rankings[rankingKey]
        i += 1

    # Sort the rankings array in order of greatest to least position.
    numRankings = len(rankingsArray)
    curPos = 0
    curGreatestPos = -1
    curGreatestPosIndex = 0
    i = 0
    while (i < numRankings - 1):
        curPos = rankingsArray[i].position
        k = i + 1
        while (k < numRankings):
            if (rankingsArray[k].position > curGreatestPos):
                curGreatestPos = rankingsArray[k].position
                curGreatestPosIndex = k
            k += 1  # Increment k.

        if (curPos < curGreatestPos):
            tmp = rankingsArray[i]
            rankingsArray[i] = rankingsArray[curGreatestPosIndex]
            rankingsArray[curGreatestPosIndex] = tmp
        i += 1  # Increment i.
    return rankingsArray


def getQualRankingsByPosition(gp, events=None):
    # Rankings are stored as rankings[driver_id] = Ranking
    rankings = {}
    if (events is None):
        events = Event.objects.filter(gp_id=gp.id)

    for event in events:
        if (event.driver_id not in rankings):
            rankings[event.driver_id] = Ranking(
                driverID=event.driver_id,
                points=0,
                position=event.qualifying.position
            )
            rankings[event.driver_id].fastestLap = event.qualifying.fastestLap

    # Convert the dictionary to a list
    rankingsArray = [None] * len(rankings)
    i = 0
    for rankingKey in rankings:
        rankingsArray[i] = rankings[rankingKey]
        i += 1

    # Sort the rankings array in order of greatest to least position.
    numRankings = len(rankingsArray)
    curPos = 0
    curGreatestPos = -1
    curGreatestPosIndex = 0
    i = 0
    while (i < numRankings - 1):
        curPos = rankingsArray[i].position
        k = i + 1
        while (k < numRankings):
            if (rankingsArray[k].position > curGreatestPos):
                curGreatestPos = rankingsArray[k].position
                curGreatestPosIndex = k
            k += 1  # Increment k.

        if (curPos < curGreatestPos):
            tmp = rankingsArray[i]
            rankingsArray[i] = rankingsArray[curGreatestPosIndex]
            rankingsArray[curGreatestPosIndex] = tmp
        i += 1  # Increment i.
    return rankingsArray


# Rankings are stored in the format of key-value:
# Key = driverID
# Value = Ranking
# sorted from greatest to least IN TERMS OF POINTS.
def getRankingsByPoints(gp):
    # Rankings are stored as rankings[driver_id] = Ranking
    rankings = {}
    events = Event.objects.filter(gp_id=gp.id)
    pointsToAdd = 0
    for event in events:
        pointsToAdd = 0
        if (event.driver_id not in rankings):
            rankings[event.driver_id] = Ranking(driverID=event.driver_id, points=0)

        pointsToAdd += event.race.points
        if (gp.type == GP.GPType.SPRINT):
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


# Rankings are stored in the format of key-value:
# Key = driverID
# Value = Ranking
# sorted from greatest to least IN TERMS OF POINTS.
def getRaceRankingsByPoints(gp, events=None):
    # Rankings are stored as rankings[driver_id] = Ranking
    rankings = {}
    if (events is None):
        events = Event.objects.filter(gp_id=gp.id)

    for event in events:
        if (event.driver_id not in rankings):
            rankings[event.driver_id] = Ranking(
                driverID=event.driver_id,
                points=0,
                position=event.race.position,
                totalTime=event.race.totalTime
            )

        rankings[event.driver_id].points += event.race.points

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
            k += 1  # Increment k.

        if (curPoints < curGreatestNum):
            tmp = rankingsArray[i]
            rankingsArray[i] = rankingsArray[curGreatestNumIndex]
            rankingsArray[curGreatestNumIndex] = tmp
        i += 1  # Increment i.
    return rankingsArray


# Rankings are stored in the format of key-value:
# Key = driverID
# Value = Ranking
# sorted from greatest to least IN TERMS OF POINTS.
def getSprintRankingsByPoints(gp, events=None):
    if (gp.type == GP.GPType.NON_SPRINT): return None

    # Rankings are stored as rankings[driver_id] = Ranking
    rankings = {}
    if (events is None):
        events = Event.objects.filter(gp_id=gp.id)

    for event in events:
        if (event.sprint is not None): # Make sure that they have raced in a Sprint.
            if (event.driver_id not in rankings):
                rankings[event.driver_id] = Ranking(
                    driverID=event.driver_id,
                    points=0,
                    position=event.sprint.position,
                    totalTime=event.sprint.totalTime
                )

            rankings[event.driver_id].points += event.sprint.points

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
            k += 1  # Increment k.

        if (curPoints < curGreatestNum):
            tmp = rankingsArray[i]
            rankingsArray[i] = rankingsArray[curGreatestNumIndex]
            rankingsArray[curGreatestNumIndex] = tmp
        i += 1  # Increment i.
    return rankingsArray
