from django.db import models

# MapDatabase is a database for a map's html (html with map in a string format)

class MapDatabase(models.Model):

    html_string = models.TextField()

    def __str__(self):
        return self.html_string
