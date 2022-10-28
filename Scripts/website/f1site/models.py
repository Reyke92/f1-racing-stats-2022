from asyncio.windows_events import NULL
from django.db import models


class GP(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    name = models.CharField(max_length=60, null=False)
    event = models.ForeignKey('Event', null=False, on_delete=models.CASCADE)
    track = models.ForeignKey('Track', null=False, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(null=False)

    def __str__(self):
        return f'{self.track.name} ({self.date})'


class Track(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    name = models.CharField(max_length=40, null=False)
    country = models.CharField(max_length=25, null=False)

    def __str__(self):
        return f'{self.name} ({self.country})'


class Event(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    driver = models.ForeignKey('Driver', null=False, on_delete=models.CASCADE)
    
    # Driver Team: the team the driver was playing for within this particular race.
    driverTeam = models.ForeignKey('Team', null=False, on_delete=models.CASCADE)
    
    # Qualificaiton Race Rank: how well the driver did in the qualification race.
    qualRank = models.PositiveSmallIntegerField(null=False)

    # Sprint Race Rank: how well the driver did in the sprint race.
    sprintRank = models.PositiveSmallIntegerField(null=True)

    # (Final) Race Rank: how well the driver did in the final race.
    raceRank = models.PositiveSmallIntegerField(null=False)

    # Qualification Points: the amount of points earned from the qualification race.
    qualPoints = models.PositiveSmallIntegerField(null=False)

    # Sprint Points: the amount of points earned from the sprint race.
    sprintPoints = models.PositiveSmallIntegerField(null=True)

    # (Final) Race Points: the amount of points earned from the final race.
    racePoints = models.PositiveSmallIntegerField(null=False)

    def __str__(self):
        totalPoints = self.racePoints + self.qualPoints
        if (self.sprintPoints != NULL): totalPoints += self.sprintPoints

        return f'({self.driver}) ({self.driverTeam}) ({totalPoints} points total)'


class Driver(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    firstName = models.CharField(max_length=30, null=False)
    lastName = models.CharField(max_length=40, null=False)
    team = models.ForeignKey('Team', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Team(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    name = models.CharField(max_length=30, null=False)
    hq = models.CharField(max_length=25, null=False)

    def __str__(self):
        return f'{self.name}'
