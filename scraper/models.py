from django.db import models

class Article(models.Model):
    source = models.CharField(max_length = 2002)
    article_id = models.IntegerField(default=0)
    url = models.URLField()
    title = models.CharField(max_length = 250)
    content = models.TextField()

    def __str__(self):
        return self.title
