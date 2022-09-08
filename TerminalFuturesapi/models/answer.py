from django.db import models

class Answer(models.Model):
    text = models.CharField(max_length=550)