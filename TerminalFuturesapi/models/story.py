from django.db import models
from django.contrib.auth.models import User

class Story(models.Model):
    title = models.CharField(max_length=40)
    startScene = models.ForeignKey("Scene", on_delete=models.CASCADE, related_name="Stories")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
