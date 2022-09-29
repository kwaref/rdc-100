from django.db import models

# Create your models here.


class Clip(models.Model):
    # title = models.CharField(max_length=100)
    # content = models.TextField()
    # image = models.FileField()
    clip = models.FileField()

    def __str__(self):
        return self.title
