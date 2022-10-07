from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Sensor(models.Model):
    _id = models.AutoField(primary_key = True, editable = True)
    name = models.CharField( max_length = 200, null = False, blank = False)
    value = models.DecimalField(max_digits = 7, decimal_places = 2, null = True, blank = True)

    def __str__(self):
        return(self.name)
