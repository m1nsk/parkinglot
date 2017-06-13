from django.db import models
from apps.parking.models import AutoCard

# Create your models here.


class Inventorization(models.Model):
    inventoriztion = models.ManyToManyField(AutoCard)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ': '.join([str(self.date), str(self.pk)])
