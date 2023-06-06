from django.shortcuts import render
from django.http import JsonResponse
from watchlist.models import Movie

# Create your views here.
def movie_list(request):
    """
    The method for handling the complete list of movies.
    Takes the request and returns the JSON response by manually converting the object into JSON.

    Args:
        request (Request): request object

    Returns:
        JsonResponse: JSON object containing data
    """    
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())

    }
    return JsonResponse(data)

def movie_details(request, pk):
    """
    The method for handling the individual movie.
    Takes the request and returns the JSON response by manually converting the object into JSON.

    Args:
        request (Request): request object

    Returns:
        JsonResponse: JSON object containing data
    """    
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active
    }
    return JsonResponse(data)