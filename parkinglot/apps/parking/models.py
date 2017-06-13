from django.db import models

# Create your models here.


class CarModel(models.Model):
    model = models.CharField(max_length=30)

    def __str__(self):
        return self.model


class CarColor(models.Model):
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.color


class CarOwner(models.Model):
    name = models.CharField(max_length=50)
    ownerInfo = models.TextField(null=True, blank=True)
    contactPerson = models.CharField(max_length=50, null=True, blank=True)
    contactTel = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class AutoCard(models.Model):
    regNumber = models.IntegerField(unique=True)
    model = models.ForeignKey(CarModel)
    color = models.ForeignKey(CarColor)
    owner = models.ForeignKey(CarOwner, on_delete=models.SET_NULL, blank=True, null=True)
    isOur = models.BooleanField()

    class Meta:
        unique_together = (("id", "regNumber"),)

    def __str__(self):
        return str(self.regNumber)


class Entry(models.Model):
    autoCad = models.ForeignKey(AutoCard)
    receivingParty = models.ForeignKey(CarOwner, blank=True, null=True)
    enter = models.DateTimeField(auto_now_add=True)
    leave = models.DateTimeField(null=True, blank=True)


