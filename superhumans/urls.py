from django.urls import path

from . import views

urlpatterns = [
  path('heroes/', views.heroes_list, name='heroes_list'),
  path('heroes/<int:key>/', views.heroes_detail, name='heroes_detail'),
]