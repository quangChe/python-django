from superhumans.models import Heroes, Villains
from superhumans.serializers import HeroesSerializer, VillainsSerializer
from rest_framework import generics

class HeroesList(generics.ListCreateAPIView):
  """
  List all heroes, or create a new hero
  """
  queryset = Heroes.objects.all()
  serializer_class = HeroesSerializer

class HeroesDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  Retrieve, update and delete a specific hero
  """
  queryset = Heroes.objects.all()
  serializer_class = HeroesSerializer

class VillainsList(generics.ListCreateAPIView):
  """
  List all villains or create a new villain
  """
  queryset = Villains.objects.all()
  serializer_class = VillainsSerializer

class VillainsDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  Retrieve, update and delete a specific villain
  """
  queryset = Villains.objects.all()
  serializer_class = VillainsSerializer