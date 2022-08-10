from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie'),
    path('director', views.show_all_directors, name='director'),
    path('director/<slug:slug_director>', views.show_one_director, name='one_director'),
    path('actors', views.show_all_actors, name='actors'),
    path('actors/<slug>', views.DetailActor.as_view(), name='one_actor'),
]