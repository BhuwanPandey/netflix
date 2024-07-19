import random
from django.shortcuts import render
from movies.models import MovieList,Movies
from django.db.models import Prefetch
from django.http import Http404
from django.shortcuts import get_object_or_404

def common(request):
    queryset =  MovieList.objects.prefetch_related(
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

def home(request):
    # if request.user.is_authenticated:
    context = common(request)
    return render(request,"home.html",context)
    # else:
    #     return redirect("/register")

def watch(request,id):
    movie = get_object_or_404(Movies,id=id)
    return render(request,"watch.html",{"movie":movie})

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
    context = common(request)
    context["title"] = data
    context["genre"] = True
    return render(request,"home.html",context)

def moviedetail(request,name,id):
    context = dict()
    if name == "movies":
        data = "movies"
        val = False
    elif name == "series":
        data = "series"
        val = True
    else:
        raise Http404
    if id:
        context["qs"] = Movies.objects.filter(id=id,isseries=val)
    context["title"] = data
    context["genre"] = True
    return render(request,"moviedetail.html",context)
