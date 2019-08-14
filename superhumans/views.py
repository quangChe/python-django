from superhumans.models import Heroes, Villains
from superhumans.serializers import HeroesSerializer, VillainsSerializer
from rest_framework import mixins, generics

class HeroesList(mixins.ListModelMixin, 
                 mixins.CreateModelMixin, 
                 generics.GenericAPIView):
  """
  List all heroes, or create a new hero.
  """

  queryset = Heroes.objects.all()
  serializer_class = HeroesSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class HeroesDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
  """
  Retrieve, update and delete
  """

  queryset = Heroes.objects.all()
  serializer_class = HeroesSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)
  