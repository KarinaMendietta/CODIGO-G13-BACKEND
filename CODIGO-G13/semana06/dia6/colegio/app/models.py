from djongo import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)