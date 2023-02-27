from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    gitlink = models.CharField(max_length=100)
    livelink = models.CharField(max_length=100)
