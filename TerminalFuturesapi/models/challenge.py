from django.db import models

class Challenge(models.Model):
    name=models.CharField(max_length=50)
    text=models.CharField(max_length=550)
    challengeAnswer=models.ForeignKey("Answer", on_delete=models.CASCADE, related_name='challenge')

