from django.db import models

# Create your models here.


class Sport(models.Model):
    sport_name = models.CharField(max_length = 100, primary_key = True)
    def __str__(self):
        return self.sport_name


class Club(models.Model):
    sport_name = models.ForeignKey(Sport, on_delete = models.CASCADE)
    club_name = models.CharField(max_length = 100)
    url = models.URLField()
    est_date = models.DateField()
    email = models.EmailField(default = '')
    
    def __str__(self):
        return self.club_name

    

class Player(models.Model):
    club_name = models.CharField(max_length = 100)
    player_name = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()
    trophies = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

    def __str__(self):
        return self.club_name
    def __str__(self):
        return self.player_name