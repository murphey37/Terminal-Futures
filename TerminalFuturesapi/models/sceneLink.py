from django.db import models

class SceneLink(models.Model):
    scene= models.ForeignKey("Scene", on_delete=models.CASCADE, related_name= "SceneLinks")
    action = models.CharField (max_length=100)
    challengeText = models.CharField (max_length=550)
    challengeAnswer = models.CharField (max_length=100)
    failScene = models.ForeignKey("Scene", on_delete=models.CASCADE, related_name="FailScene")
    nextScene=models.ForeignKey("Scene", on_delete=models.CASCADE, related_name="NextScene")


