"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from TerminalFuturesapi.models import SceneLink, UserScene

class UserSceneView(ViewSet):
    """Level up game view"""


    def retrieve(self, request, pk):
        """Handle GET requests for single userScene
        Returns:
            Response -- JSON serialized userScene
        """
        try:
            userScene = UserScene.objects.get(pk=pk)
            serializer = UserSceneSerializer(userScene)
            return Response(serializer.data)
        except UserScene.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
        

    def list(self, request):
        """Handle GET requests to get all games
        Returns:
            Response -- JSON serialized list of games
        """
        userScenes = UserScene.objects.all()
        sceneLink = request.query_params.get('sceneLink', None)
        if sceneLink is not None:
            userScenes = UserScene.filter(sceneLink_id=sceneLink)
        serializer = UserSceneSerializer(userScenes, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized game instance
        """

        sceneLink = SceneLink.objects.get(pk=request.data["sceneLink"])
        user = User.objects.get(user=request.auth.user)
        userScene = UserScene.objects.create(
            success=request.data["success"],
            sceneLink=sceneLink,
            user=user
        )
        serializer = UserSceneSerializer(userScene)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """

        userScene = UserScene.objects.get(pk=pk)
        userScene.success = request.data["success"]
        sceneLink = SceneLink.objects.get(pk=request.data["sceneLink"])
        user = User.objects.get(user=request.auth.user)
        userScene.sceneLink = sceneLink
        userScene.user = user
        sceneLink.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        userScene = UserScene.objects.get(pk=pk)
        userScene.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
            

class UserSceneSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = UserScene
        fields = ('id', 'sceneLink', 'user', 'success')
        depth = 1