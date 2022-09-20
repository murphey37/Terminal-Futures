from django.db import models
from .scene import Scene

class SceneLink(models.Model):
    scene= models.ForeignKey(Scene, on_delete=models.CASCADE, related_name= "scene_links")
    action = models.CharField (max_length=100, null=True)
    challengeText = models.CharField (max_length=550, null=True)
    challengeAnswer = models.CharField (max_length=100, null=True)
    failScene = models.ForeignKey(Scene, on_delete=models.CASCADE, related_name="FailScene", null=True)
    nextScene=models.ForeignKey(Scene, on_delete=models.CASCADE, related_name="NextScene", null=True)


