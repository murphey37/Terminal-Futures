from django.db import models

class Scene(models.Model):
    name = models.CharField(max_length=40)
    sceneText = models.CharField(max_length=550)

