from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from superhumans.models import Heroes
from superhumans.serializers import HeroesSerializer

@api_view(['GET', 'POST'])
def heroes_list(request):
  '''
  List all heroes, or create a new hero
  '''
  if request.method == 'GET':
    heroes = Heroes.objects.all()
    serializer = HeroesSerializer(heroes, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = HeroesSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', ])
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