import datetime

from django.db import models
from django.utils import timezone


class Posts(models.Model):
    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('작성일자')
    author = models.CharField(max_length=10)
    content = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    place_id = models.IntegerField(default=0)

# Create your models here.
