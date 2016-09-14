from django.db import models

# Create your models here.
class Planets(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name
