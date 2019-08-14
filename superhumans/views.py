from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from superhumans.models import Heroes, Villains
from superhumans.serializers import HeroesSerializer, VillainsSerializer


class HeroesList(APIView):
  """
  List all heroes, or create a new hero.
  """
  def get(self, request, format=None):
    heroes = Heroes.objects.all()
    serializer = HeroesSerializer(heroes, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = HeroesSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def heroes_detail(request, key):
  '''
  Retrieve, update or delete a single hero
  '''
  try: 
    heroes = Heroes.objects.get(pk=key)
  except Heroes.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = HeroesSerializer(heroes)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = HeroesSerializer(heroes, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    heroes.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)