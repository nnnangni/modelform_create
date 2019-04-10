from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    content1 = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()