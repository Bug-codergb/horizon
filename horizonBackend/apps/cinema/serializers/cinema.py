from rest_framework.serializers import ModelSerializer
from apps.cinema.models import Cinema
from apps.user.serializers.user import UserSerializer
from .tag import TagSerializer
class CinemaSerializer(ModelSerializer):
  user = UserSerializer()
  tag = TagSerializer(many=True)
  class Meta:
    model = Cinema
    fields=["id","name","alias","address","createTime","user","tag"]