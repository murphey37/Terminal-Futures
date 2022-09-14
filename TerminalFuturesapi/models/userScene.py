from django.db import models
from django.contrib.auth.models import User

from TerminalFuturesapi.models.sceneLink import SceneLink

class UserScene(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sceneLink = models.ForeignKey("Scenelink", on_delete=models.CASCADE, related_name="userScene")
    success= models.BooleanField()

