from rest_framework.serializers import ModelSerializer,SerializerMethodField
from apps.actor.models import Actor,ActorDeductive
from apps.file.serializers.file import FileSerializer

class ActorDeductiveSerializer(ModelSerializer):
  class Meta:
    model = ActorDeductive
    fields=["year","description"]

class ActorSerializer(ModelSerializer):
  avatar = FileSerializer()
  deductive = ActorDeductiveSerializer(many=True,source="actordeductive_set")
  class Meta:
    model = Actor
    fields = [
      "id","name","description","birthday","birthplace","identity","gender","nationality","people",
      "height","constellation","school","company","avatar","deductive"
    ]