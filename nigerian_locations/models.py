from django.db import models


class State(models.Model):
    name = models.CharField(max_length=255)

class LGA(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class Area(models.Model):
    name = models.CharField(max_length=255)
    lga = models.ForeignKey(LGA, on_delete=models.SET_NULL, blank=True, null=True)

class Localities(models.Model):
    name = models.CharField(max_length=255)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, blank=True, null=True)