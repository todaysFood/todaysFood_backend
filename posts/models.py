import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings


class Posts(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200, verbose_name="제목")
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='작성일자')
    # author = models.CharField(max_length=25, null=True, verbose_name="작성자")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE, to_field="id", db_column='author', null=True, verbose_name="작성자")
    content = models.TextField(max_length=300, verbose_name="내용")
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="평점")
    place_id = models.IntegerField(default=0)
# Create your models here.
