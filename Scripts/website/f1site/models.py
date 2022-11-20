from django.db import models


class GP(models.Model):
    class GPType(models.IntegerChoices):
        NON_SPRINT = 0
        SPRINT = 1

    # id = models.BigAutoField() <--- PRIMARY KEY
    name = models.CharField(max_length=45, null=False)
    track = models.ForeignKey('Track', null=False, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(null=False)
    type = models.PositiveSmallIntegerField(choices=GPType.choices, null=False)

    def __str__(self):
        return f'{self.track.name} ({self.date})'


class Track(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    name = models.CharField(max_length=45, null=False)
    location = models.CharField(max_length=45, null=False)

    def __str__(self):
        return f'{self.name} ({self.location})'


class Event(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    gp = models.ForeignKey('GP', null=False, on_delete=models.CASCADE)
    
    driver = models.ForeignKey('Driver', null=False, on_delete=models.CASCADE)
    
    # Driver Team: the team the driver was playing for within this particular race.
    driverTeam = models.ForeignKey('Team', null=True, on_delete=models.CASCADE)

    qualifying = models.ForeignKey('Qualifying', null=True, on_delete=models.DO_NOTHING)
    race = models.ForeignKey('Race', null=True, on_delete=models.DO_NOTHING)
    sprint = models.ForeignKey('Sprint', null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.gp.name} - {self.driver}'


class Qualifying(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    fastestLap = models.TimeField(null=False)
    position = models.PositiveSmallIntegerField(null=False, default=0)


class Sprint(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    totalTime = models.TimeField(null=False)
    position = models.PositiveSmallIntegerField(null=False, default=0)
    points = models.FloatField(null=False)


class Race(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    totalTime = models.TimeField(null=False)
    position = models.PositiveSmallIntegerField(null=False, default=0)
    points = models.FloatField(null=False)


class Driver(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    name = models.CharField(max_length=70, null=False)
    abvr = models.CharField(max_length=3, null=False)
    team = models.ForeignKey('Team', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Team(models.Model):
    # id = models.BigAutoField() <--- PRIMARY KEY
    name = models.CharField(max_length=45, null=False)

    def __str__(self):
        return f'{self.name}'
