from django.db import models

# Create your models here.
class MapDatabase(models.Model):

    html_string = models.TextField()

    def __str__(self):
        return self.html_string
