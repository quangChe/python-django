from django.urls import path

from . import views

urlpatterns = [
  path('heroes/', views.HeroesList.as_view(), name='heroes_list'),
  path('heroes/<int:pk>/', views.HeroesDetail.as_view(), name='heroes_detail'),
  path('villains/', views.VillainsList.as_view(), name='villains_list'),
  path('villains/<int:pk>/', views.VillainsDetail.as_view(), name='villains_detail'),
]