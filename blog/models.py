from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 1000)
    description = models.TextField()
    date = models.DateField()
