from django.urls import path
from . import views

urlpatterns = [
    # path for the complete list of movies
    path('list', views.MoviesListAV.as_view(), name='movie-list'),
    # path for the individual movie element
    path('<int:pk>', views.MovieDetailAV.as_view(), name='movie-details'),
]