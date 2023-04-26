from django.urls import path
from movies.views import MovieListView, MovieCreateView

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/create/', MovieCreateView.as_view(), name='movie-create'),
]
