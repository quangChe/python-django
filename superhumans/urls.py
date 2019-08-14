from django.urls import path

from . import views

urlpatterns = [
  path('heroes/', views.HeroesList.as_view(), name='heroes_list'),
  path('heroes/<int:key>/', views.heroes_detail, name='heroes_detail'),
]