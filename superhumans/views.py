from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from superhumans.models import Heroes
from superhumans.serializers import HeroesSerializer

# Remove csrf_exempt for production (bad!)
@csrf_exempt
def heroes_list(request):
  '''
  List all heroes, or create a new hero
  '''
  if request.method == 'GET':
    heroes = Heroes.objects.all()
    serializer = HeroesSerializer(heroes, many=True)
    return JsonResponse(serializer.data, safe=False)
  # elif request.method == 'POST':

def heroes_detail(request, key):
  '''
  Retrieve, update or delete a single hero
  '''
  try: 
    heroes = Heroes.objects.get(pk=key)
  except Heroes.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = HeroesSerializer(heroes)
    return JsonResponse(serializer.data)