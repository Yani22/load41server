from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

class Trackers_Info(models.Model):
    trackersInfoId = models.CharField(max_length=1000, blank=True, null=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    createdAt = models.DateTimeField(default=datetime.now)
    datetime = models.DateTimeField(default=datetime.now)
    deliveryProofPhotos = models.ImageField(upload_to='images/', null=True,blank=True)
    dispatcher = models.CharField(max_length=1000, blank=True, null=True)
    driver = models.CharField(max_length=1000, blank=True, null=True)
    driverPhoneNumber = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=1000, blank=True, null=True)
    equipmentType = models.CharField(max_length=1000, blank=True, null=True)
    isDeleted = models.BooleanField(default=False)
    latestAvailability = models.CharField(max_length=1000, blank=True, null=True)
    loadId = models.CharField(max_length=1000, blank=True, null=True)
    loadStatus = models.CharField(max_length=1000, blank=True, null=True)
    locationLogs = models.CharField(max_length=1000, blank=True, null=True)

# class Location_Logs(models.Model):
#     locationLogId = models.CharField(max_length=1000, blank=True, null=True)
#     lat = models.CharField(max_length=1000, blank=True, null=True)
#     lng = models.CharField(max_length=1000, blank=True, null=True)
#     price = models.CharField(max_length=1000, blank=True, null=True)

    # Define other fields as needed