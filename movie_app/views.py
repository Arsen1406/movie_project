from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from django.views.generic import ListView, DetailView


def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').desc(nulls_last=True))
    movies = Movie.objects.annotate(
        new_field_True=Value(True),
        new_field_False=Value(False),
        new_field_str=Value('Hello, World!'),
        new_field_int=Value(456),
        new_budget=F('budget') + 100,
        sum_rating_year=F('rating') + F('year'),

    )
    agg = movies.aggregate(Max('rating'), Min('rating'), Avg('budget'))
    return render(request, 'movie_app/mov.html', {
        'movies': movies,
        'agg': agg
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })


def show_all_directors(request):
    director = Director.objects.all()
    return render(request, 'movie_app/director.html', {
        'director': director
    })


def show_one_director(request, slug_director: str):
    director = get_object_or_404(Director, slug=slug_director)
    return render(request, 'movie_app/one_direc.html', {
        'director': director
    })

def show_all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/actors.html', {
        'actors': actors
    })


# def show_one_actor(request, slug_actor: str):
#     actor = get_object_or_404(Actor, slug=slug_actor)
#     return render(request, 'movie_app/one_actor.html', {
#         'actor': actor
#     })

class DetailActor(DetailView):
    template_name = 'movie_app/one_actor.html'
    model = Actor

