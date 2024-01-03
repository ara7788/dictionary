from django.db import models
from ckeditor.fields import RichTextField

class Home(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(blank=True)
    description = RichTextField(blank=True)
    sources = RichTextField(blank=True)

    def __str__(self):
        return self.title
