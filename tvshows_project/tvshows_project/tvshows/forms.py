from django.forms import ModelForm
from .models import TVShow

class TVShowForm(ModelForm):
    class Meta:
        model = TVShow
        fields = ['title', 'genre', 'description', 'release_date', 'rating', 'photo','seasons','episodes_per_season']
