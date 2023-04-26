from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .models import Movie
from .serializers import MovieSerializer

class MovieListView(generics.ListAPIView):
    """
    Returns a list of trending movies sorted by ranking.
    """
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.order_by('-ranking')

class MovieCreateView(generics.CreateAPIView):
    """
    Adds a new movie instance to the cinema program.
    """
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)
