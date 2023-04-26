from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Movie
from .serializers import MovieSerializer  
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['cinema']

@receiver(post_save, sender=Movie)
def create_or_update_movie_in_mongodb(sender, instance, created, **kwargs):
    """
    Create or update the movie instance in MongoDB.
    """
    collection = db['movies']
    data = MovieSerializer(instance).data
    data.pop('id', None)
    if created:
        collection.insert_one(data)
    else:
        collection.replace_one({'name': instance.name}, data)

@receiver(post_delete, sender=Movie)
def delete_movie_in_mongodb(sender, instance, **kwargs):
    """
    Delete the movie instance from MongoDB.
    """
    collection = db['movies']
    collection.delete_one({'name': instance.name})

