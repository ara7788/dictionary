from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
import datetime

class Article(models.Model):
    title = models.CharField(max_length=100)
    cdate = models.DateTimeField(default=datetime.datetime.now())
    mdate = models.DateTimeField(auto_now=True)
    description = RichTextField()
    sources = RichTextField(blank=True)
    slug = models.SlugField(null=True,max_length=255,unique=False,db_index=True)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article:article_detail', kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)