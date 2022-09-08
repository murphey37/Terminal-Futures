from django.db import models

class Action(models.Model):
    text = models.CharField(max_length=550)