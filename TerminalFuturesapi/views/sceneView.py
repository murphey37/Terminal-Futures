"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from TerminalFuturesapi.models import Scene, Story, SceneLink, sceneLink


class SceneView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            scene = Scene.objects.get(pk=pk)
            serializer = SceneSerializer(scene)
            return Response(serializer.data)
        except scene.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
        

    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
            Response -- JSON serialized list of game types
        """
        scenes = Scene.objects.all()
        story = request.query_params.get('story', None)
        if story is not None:
            scenes = scenes.filter(story_id=story)
        serializer = SceneSerializer(scenes, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized game instance
        """

        story = Story.objects.get(pk=request.data["story"])

        scene = Scene.objects.create(
            name=request.data["name"],
            sceneText=request.data["sceneText"],
            story=story
        )
        serializer = SceneSerializer(scene)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a scene
        Returns:
            Response -- Empty body with 204 status code
        """
        story = Story.objects.get(pk=request.data["story"])

        scene = Scene.objects.get(pk=pk)
        scene.name = request.data["name"]
        scene.sceneText = request.data["sceneText"]
        scene.story = story
        scene.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        scene = Scene.objects.get(pk=pk)
        scene.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
            

class SceneSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Scene
        fields = ('id', 'name', 'sceneText','story', 'scene_links')
        depth = 1