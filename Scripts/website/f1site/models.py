from django.db import models


class GP(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    track = models.ForeignKey('Track', null=False, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(null=False)

    def __str__(self):
        return f'{self.track.name} ({self.date})'


class Track(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    name = models.CharField(max_length=60, null=False)
    location = models.ForeignKey('Location', null=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Location(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    address = models.CharField(max_length=100, null=False)
    zipcode = models.PositiveSmallIntegerField(null=False)
    state = models.ForeignKey('State', null=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.address}, {self.state.acronym} {self.zipcode}'


class State(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    acronym = models.CharField(max_length=2, null=False)
    name = models.CharField(max_length=14, null=False)

    def __str__(self):
        return self.name


# Qualification Race.
class QualRace(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    gp = models.ForeignKey('GP', null=False, on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', null=False, on_delete=models.CASCADE)
    # Ranking: how well the driver did in this race.
    ranking = models.PositiveSmallIntegerField(null=False)
    # Points Earned: the amount of points earned from this particular race.
    pointsEarned = models.PositiveSmallIntegerField(null=False)
    # Driver Team: the team the driver was playing for within this particular race.
    driverTeam = models.ForeignKey('Team', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.gp} ({self.driver}) ({self.driverTeam})'


class SprintRace(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    gp = models.ForeignKey('GP', null=False, on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', null=False, on_delete=models.CASCADE)
    # Ranking: how well the driver did in this race.
    ranking = models.PositiveSmallIntegerField(null=False)
    # Points Earned: the amount of points earned from this particular race.
    pointsEarned = models.PositiveSmallIntegerField(null=False)
    # Driver Team: the team the driver was playing for within this particular race.
    driverTeam = models.ForeignKey('Team', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.gp} ({self.driver}) ({self.driverTeam})'


class Race(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    gp = models.ForeignKey('GP', null=False, on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', null=False, on_delete=models.CASCADE)
    # Ranking: how well the driver did in this race.
    ranking = models.PositiveSmallIntegerField(null=False)
    # Points Earned: the amount of points earned from this particular race.
    pointsEarned = models.PositiveSmallIntegerField(null=False)
    # Driver Team: the team the driver was playing for within this particular race.
    driverTeam = models.ForeignKey('Team', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.gp} ({self.driver}) ({self.driverTeam})'


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

    def __str__(self):
        return f'{self.name}'
