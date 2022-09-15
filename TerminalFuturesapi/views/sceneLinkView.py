"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from TerminalFuturesapi.models import Scene, SceneLink

class SceneLinkView(ViewSet):
    """Level up game view"""


    def retrieve(self, request, pk):
        """Handle GET requests for single sceneLink
        Returns:
            Response -- JSON serialized sceneLink
        """
        try:
            sceneLink = SceneLink.objects.get(pk=pk)
            serializer = SceneLinkSerializer(sceneLink)
            return Response(serializer.data)
        except SceneLink.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
        

    def list(self, request):
        """Handle GET requests to get all games
        Returns:
            Response -- JSON serialized list of games
        """
        sceneLinks = SceneLink.objects.all()
        scene = request.query_params.get('scene', None)
        if scene is not None:
            sceneLinks = sceneLinks.filter(scene_id=scene)
        serializer = SceneLinkSerializer(sceneLinks, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized game instance
        """

        scene = Scene.objects.get(pk=request.data["scene"])

        sceneLink = SceneLink.objects.create(
            action=request.data["action"],
            challengeText=request.data["challengeText"],
            challengeAnswer=request.data["challengeAnswer"],
            failScene=scene,
            nextScene=scene,
            scene=scene
        )
        serializer = SceneLinkSerializer(sceneLink)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """

        sceneLink = SceneLink.objects.get(pk=pk)
        sceneLink.action = request.data["action"]
        sceneLink.challengeText = request.data["challengeText"]
        sceneLink.challengeAnswer = request.data["challengeAnswer"]

        scene = Scene.objects.get(pk=request.data["scene"])
        sceneLink.scene = scene
        sceneLink.failScene = scene
        sceneLink.nextScene = scene
        sceneLink.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        sceneLink = SceneLink.objects.get(pk=pk)
        sceneLink.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
            

class SceneLinkSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = SceneLink
        fields = ('id', 'scene', 'action', 'challengeText', 'challengeAnswer', 'failScene', 'nextScene')
        depth = 1
