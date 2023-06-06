from django.urls import path
from . import views

urlpatterns = [
    # path for the complete list of movies
    path('list', views.movie_list, name='movie-list'),
    # path for the individual movie element
    path('<int:pk>', views.movie_details, name='movie-details'),
]