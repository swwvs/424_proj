from django.db import models

class TVShow(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    photo = models.ImageField(upload_to='tv_shows/', null=True, blank=True) # For uploading images
    seasons = models.PositiveIntegerField(default=1)  # Number of seasons
    episodes_per_season = models.PositiveIntegerField(default=1)  # Episodes per season

    def __str__(self):
        return self.title
