from django.db import models

class ChallengeResource(models.Model):
    challenge = models.ManyToManyField("Challenge")
    resource = models.ManyToManyField("Resource") #am I referencing the wrong way with capitals?