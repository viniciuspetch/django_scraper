from django.db import models

class Article(models.Model):
    article_id = models.IntegerField(default=0)
    url = models.URLField()
    title = models.CharField(max_length = 250)
