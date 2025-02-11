from django.db import models

# Create your models here.
class Chapter(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=200)
    chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank =True)

    def __str__(self):
        return self.name

