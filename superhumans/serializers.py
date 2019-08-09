from rest_framework import serializers
from superhumans.models import Heroes, Villains

class HeroesSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  alias = serializers.CharField(max_length=100)
  real_name = serializers.CharField(max_length=100)
  superpower = serializers.CharField(max_length=400)
  hero_tier = serializers.IntegerField(max_value=10, min_value=1)
  nemesis = serializers.PrimaryKeyRelatedField(read_only=True)

  def create(self, valid_data):
    '''
    Create and return a new `Heroes` instance, given the validated data
    '''
    return Heroes.objects.create(**valid_data)

  def update(self, instance, valid_data):
    '''
    Update and return a `Heroes` instance, given the validated data
    '''
    instance.alias = valid_data.get('alias', instance.alias)
    instance.real_name = valid_data.get('real_name', instance.real_name)
    instance.superpower = valid_data.get('superpower', instance.superpower)
    instance.hero_tier = valid_data.get('hero_tier', instance.hero_tier)
    instance.save()
    return instance


class VillainsSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  alias = serializers.CharField(max_length=100)
  real_name = serializers.CharField(max_length=100)
  superpower = serializers.CharField(max_length=400)
  threat_level = serializers.IntegerField(max_value=10, min_value=1)

  def create(self, valid_data):
    '''
    Create and return a new `Villains` instance, given the validated data
    '''
    return Villains.objects.create(**valid_data)
  
  def update(self, instance, valid_data):
    '''
    Update and return a `Heroes` instance, given the validated data
    '''
    instance.alias = valid_data.get('alias', instance.alias)
    instance.real_name = valid_data.get('real_name', instance.real_name)
    instance.superpower = valid_data.get('superpower', instance.superpower)
    instance.threat_level = valid_data.get('threat_level', instance.threat_level)
    instance.save()
    return instance