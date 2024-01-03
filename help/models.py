from django.db import models
from ckeditor.fields import RichTextField
import datetime

class Help(models.Model):
    title = models.CharField(max_length=100)
    anchor = models.CharField(max_length=60,blank=True)
    cdate = models.DateTimeField(default=datetime.datetime.now())
    mdate = models.DateTimeField(auto_now=True)
    description = RichTextField(blank=True)
    

    def __str__(self):
        return self.title