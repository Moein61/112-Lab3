from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Movie, Genre
# Create your views here.

def index(request):
    return render(request, 'views/index.html')

def catalog(request):
    movies = Movie.objects.all()
    #titles = ', '.join([m.title for m in movies])
    #return HttpResponse(titles)
    return render(request, 'views/catalogtest.html', {'title' : 'FROM BACKED', 'movies': movies })


def test (requst):
    return HttpResponse("this is a test page!")

def developer(request):
    return HttpResponse("<h1>Moein Ghomeshian</h1>")