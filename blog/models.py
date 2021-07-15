from datetime import timezone
import datetime
from django.db import models
from django.utils.text import slugify
from django.utils.timezone import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=30, default="")
    author= models.CharField(max_length=50, default="Túlio Farias")
    #text=models.TextField(max_length=3000, default="")
    text=RichTextField()
    datetime=models.DateTimeField(default=datetime.now)
    slug=models.SlugField(default='', blank=True, null=False, db_index=True)

    
