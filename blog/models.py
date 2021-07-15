from django.db import models
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    author= models.CharField(max_length=50)
    text=models.TextField(max_length=3000)
    date=models.DateTimeField()
    slug=models.SlugField(default='', blank=True, null=False, db_index=True)
    