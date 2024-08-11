import random
from django.shortcuts import render,redirect
from movies.models import MovieList,Movies
from django.db.models import Prefetch,Count
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def common(request):
    queryset =  MovieList.objects.annotate(total_movies=Count('content')).prefetch_related(
        Prefetch('content', queryset=Movies.objects.all())
    )
    new_qs = list(queryset)
    random.shuffle(new_qs)
    movie_qs = list(Movies.objects.all())
    random.shuffle(movie_qs)
    context = {
        "movieslists":new_qs[:6],
        "random_movie":movie_qs[0] if movie_qs else None,
        "genre":False
    }
    return context

@login_required(login_url='/login/')
def home(request):
    context = common(request)
    return render(request,"home.html",context)

@login_required(login_url='/login/')
def watch(request,id):
    movie = get_object_or_404(Movies,id=id)
    return render(request,"watch.html",{"movie":movie})

@login_required(login_url='/login/')
def info(request,id):
    movie = get_object_or_404(Movies,id=id)
    return render(request,"info.html",{"movie":movie})

def name(request,name):
    if name == "movies":
        data = "movies"
    elif name == "series":
        data = "series"
    else:
        raise Http404
    if not request.user.is_authenticated:
        return redirect("/login/")
    context = common(request)
    context["title"] = data
    context["genre"] = True
    return render(request,"home.html",context)
