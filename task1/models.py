from django.db import models


class Football(models.Model):
    player_name = models.CharField(max_length=200)
    player_type = models.CharField(max_length=200)
    date_created = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.player_name + ' ' + self.player_type


class Cricket(models.Model):
    player_name = models.CharField(max_length=200)
    player_type = models.CharField(max_length=200)
    date_created = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.player_name + ' ' + self.player_type
