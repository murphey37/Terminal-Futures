from django.db import models

class Death(models.Model):
    name=models.CharField(max_length=50)
    text=models.CharField(max_length=550)
    challenge=models.ForeignKey("Challenge", on_delete=models.CASCADE, related_name='death')