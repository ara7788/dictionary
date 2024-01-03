from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
import datetime

class OnlineHelper(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    stream_framework_name = models.CharField(blank=True, max_length=100)
    cdate = models.DateTimeField(default=datetime.datetime.now())
    mdate = models.DateTimeField(auto_now=True)
    description = RichTextField(blank=True)
    architecture = RichTextField(blank=True)
    stream_framework_features = RichTextField(blank=True)
    sources = RichTextField(blank=True)
    slug = models.SlugField(default='',max_length=255,unique=True,db_index=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('onlinehelper:onlinehelper_detail', kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)