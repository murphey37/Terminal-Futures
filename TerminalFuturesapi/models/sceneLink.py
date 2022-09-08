from django.db import models

class SceneLink(models.Model):
    actionId = models.ForeignKey("Action", on_delete=models.CASCADE)
    challengeId = models.ForeignKey("Scene", on_delete=models.CASCADE)
    sceneId= models.ForeignKey("Scene", on_delete=models.CASCADE)
    nextSceneId=models.ForeignKey("Scene", on_delete=models.CASCADE)


