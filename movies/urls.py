
from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movieListApiView, name='movie-list'),
    path('movies/update/<int:pk>/', views.updateMovieListApi, name='update-movie-list'),
    path('movies/delete/<int:pk>/', views.deleteMovieApi, name='delete-movie'),

    path('genres/', views.genreListApiView, name='genre-list'),
    path('genres/update/<int:pk>/', views.updateGenreListApi, name='update-genre-list'),
    path('genres/delete/<int:pk>/', views.deleteGenreApi, name='delete-genre'),


]
