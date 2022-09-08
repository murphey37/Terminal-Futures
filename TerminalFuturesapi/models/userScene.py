from django.db import models

from TerminalFuturesapi.models.sceneLink import SceneLink

class UserScene(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    sceneLink = models.ManyToManyField("Scenelink")
    success= models.BooleanField

