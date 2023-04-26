from django.db import models
from datetime import datetime


class Movie(models.Model):
    name = models.CharField(max_length=100)
    protagonists = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='movie_posters/')
    start_date = models.DateField()
    STATUS_CHOICES = (
        ('coming-up', 'Coming Up'),
        ('starting', 'Starting'),
        ('running', 'Running'),
        ('finished', 'Finished')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    ranking = models.IntegerField(default=0)

    def update_ranking(self):
        """
        Updates the ranking of the movie based on its status and start date.
        """
        if self.status == 'coming-up':
            # The ranking of each movie can be faked at first
            self.ranking = 50
        elif self.status == 'starting':
            # The rank of each instance should increase by 10, once every 5 minutes
            time_difference = (datetime.now().date() - self.start_date).days
            self.ranking = 50 + (time_difference * 2)
        elif self.status == 'running':
            self.ranking = 100
        else:
            self.ranking = 0
