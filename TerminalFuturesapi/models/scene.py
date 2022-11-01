from django.db import models

class Scene(models.Model):
    name = models.CharField(max_length=40)
    sceneText = models.CharField(max_length=700)
    story = models.ForeignKey("Story", on_delete=models.CASCADE)
    # sceneLinks = models.ForeignKey("Scenelink", on_delete=models.CASCADE)
