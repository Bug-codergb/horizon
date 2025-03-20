from rest_framework.serializers import ModelSerializer
from apps.cinema.models import CinemaTag

class TagSerializer(ModelSerializer):
  class Meta:
    model = CinemaTag
    fields = "__all__"