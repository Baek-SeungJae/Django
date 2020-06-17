from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from movies.models import Movie
# Create your views here.


def movies(request):
    QuerySet = Movie.objects.all().order_by('-open_date')
    QuerySet2 = Movie.objects.all().order_by('-score')
    QuerySet3 = Movie.objects.all().order_by('-audience')
    movieList = list()
    movieList2 = list()
    movieList3 = list()
    for i in range(len(QuerySet)):
        movieList.append(QuerySet[i])
    for i in range(len(QuerySet2)):
        movieList2.append(QuerySet2[i])
    for i in range(len(QuerySet3)):
        movieList3.append(QuerySet3[i])
    context = {
        'movieList': movieList,
        'movieList2': movieList2,
        'movieList3': movieList3,
    }
    return render(request, 'movies/movies.html', context)


def new(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
        return redirect('movies:movies')
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/form.html', context)


def detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

def edit(request,id):
    movie = get_object_or_404(Movie, id = id)
    if request.method == "POST":
        form = MovieForm(request.POST,instance=movie)
        if form.is_valid():
            movie = form.save()
        return redirect('movies:movies')
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
    }
    return render(request, 'movies/form.html', context)

def delete(request,id):
    if request.method == "POST":
        movie = get_object_or_404(Movie, id = id)
        movie.delete()
    return redirect('movies:movies')