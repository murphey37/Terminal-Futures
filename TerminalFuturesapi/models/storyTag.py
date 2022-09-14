from django.db import models

class StoryTag(models.Model):
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)
    story=models.ForeignKey("Story", on_delete=models.CASCADE)
