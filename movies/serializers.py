from rest_framework import serializers
from .models import Movie, Genre

class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Movie
        fields = ('id','name','published_year','genre','watched')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'