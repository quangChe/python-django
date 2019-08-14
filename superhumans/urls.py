from django.urls import path

from . import views

urlpatterns = [
  path('heroes/', views.HeroesList.as_view(), name='heroes_list'),
  path('heroes/<int:pk>/', views.HeroesDetail.as_view(), name='heroes_detail'),
]