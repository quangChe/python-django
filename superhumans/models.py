from django.db import models

class Villains(models.Model):
  alias = models.CharField(max_length=100)
  real_name = models.CharField(max_length=100)
  superpower = models.CharField(max_length=400) 
  threat_level = models.IntegerField()

  def __str__(self):
    return self.alias 

class Heroes(models.Model):
  alias = models.CharField(max_length=100)
  real_name = models.CharField(max_length=100)
  superpower = models.CharField(max_length=400)
  hero_tier = models.IntegerField()
  nemesis = models.ForeignKey(Villains, on_delete=models.CASCADE)

  def __str__(self):
    return self.alias
  
  def can_defeat(self, villain_level):
    return (11 - villain_level >= self.hero_tier)


