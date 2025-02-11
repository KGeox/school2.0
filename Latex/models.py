from django.db import models

# Create your models here.
class LatexExpression(models.Model):
    expression = models.TextField()

    def __str__(self):
        return self.expression[:50]