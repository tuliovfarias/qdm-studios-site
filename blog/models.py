from datetime import timezone
import datetime
from django.db import models
from django.utils.text import slugify
from django.utils.timezone import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100, default="")
    author= models.CharField(max_length=50, default="Túlio Farias")
    #text=models.TextField(max_length=3000, default="")
    #text=RichTextField()
    text=RichTextUploadingField()
    datetime=models.DateTimeField(default=datetime.now)
    slug=models.SlugField(default='', blank=True, null=False, db_index=True)

    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )
    
    # def current_hit_count(self):
    #     return self.hit_count.hits

    def __str__(self):
        return f"{self.title}"

class Slide(models.Model):
    title=models.CharField(max_length=200, default="")
    photo=RichTextUploadingField()
    slug=models.SlugField(default='', blank=True, null=False, db_index=True)

    def __str__(self):
        return f"Title: {self.title}"

