from django.db import models

class Resource(models.Model):
    name=models.CharField(max_length=40)
    link=models.URLField(max_length=400)
