from django.db import models

class Api(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name
