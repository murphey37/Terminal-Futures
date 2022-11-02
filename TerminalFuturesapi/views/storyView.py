"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from TerminalFuturesapi.models import Scene, Story, SceneLink


class StoryView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            story = Story.objects.get(pk=pk)
            serializer = StorySerializer(story)
            return Response(serializer.data)
        except story.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
        

    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
            Response -- JSON serialized list of game types
        """
        stories = Story.objects.all()
        scene = request.query_params.get('scene', None)
        if scene is not None:
            stories = stories.filter(scene_id=scene)
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized game instance
        """

        # startingScene = Scene.objects.get(pk= 1)
        user = request.auth.user


        story = Story.objects.create(
            title=request.data["title"],
            startScene=None,
            user=user
        )

        newStartingScene=Scene.objects.create(
                story=story,
                name=request.data["name"],
                sceneText=request.data["sceneText"]
            )
        story.startScene = newStartingScene
        story.save()
        serializer = StorySerializer(story)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a scene
        Returns:
            Response -- Empty body with 204 status code
        """
        scene = Scene.objects.get(pk=request.data["scene"])
        user = User.objects.get(user=request.auth.user)

        story = Story.objects.get(pk=pk)
        story.title = request.data["title"]
        story.startScene = scene
        story.user = user
        story.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        story = Story.objects.get(pk=pk)
        story.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
            

class StorySerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Story
        fields = ('id', 'title', 'startScene','user')
        depth = 1

class SceneSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    story = StorySerializer(many=False)
    class Meta:
        model = Scene
        fields = ('id', 'name', 'sceneText','story')
        depth = 1