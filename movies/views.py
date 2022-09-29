from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer

@api_view(['GET','POST'])
def movieListApiView(request): 
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many = True)
    if request.method == 'POST':
        serializer = MovieSerializer( data = request.data)

        if serializer.is_valid():
            serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def updateMovieListApi(request,pk):
    movie = Movie.objects.get( id = pk)
    serializer = MovieSerializer( instance = movie, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return redirect('movie-list')

@api_view(['DELETE'])
def deleteMovieApi(request,pk):
    movie = Movie.objects.get( id = pk)
    movie.delete()

    return redirect('movie-list')


@api_view(['GET','POST'])
def genreListApiView(request): 
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many = True)

    if request.method == 'POST':
        serializer = GenreSerializer( data = request.data)
        if serializer.is_valid():
            serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def updateGenreListApi(request,pk):
    genre = Genre.objects.get( id = pk)
    serializer = GenreSerializer( instance = genre, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return redirect('genre-list')

@api_view(['DELETE'])
def deleteGenreApi(request,pk):
    genres = Genre.objects.get( id = pk)
    genres.delete()

    return redirect('genre-list')
