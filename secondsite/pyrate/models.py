from django.db import models

# Create your models here.
class Client(models.Model):
    client_version = models.CharField(max_length=200)
    securecore_version = models.CharField(max_length=200)
    ip_address = models.IPAddressField(default=None)
    occupation = models.BooleanField(default=False)
    scrambler = models.IPAddressField(default='0.0.0.0')
    start_time = models.DateTimeField('Start time')
    latest_update_time = models.DateTimeField('latest update time')


class Kms(models.Model):
    kms_version = models.CharField(max_length=200)
    ip_address = models.IPAddressField(default=None)
    occupation = models.BooleanField(default=False)
    scrambler = models.IPAddressField(default='0.0.0.0')
    client_number = models.IntegerField(default=0)
    #client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_time = models.DateTimeField('Start time')
    latest_update_time = models.DateTimeField('latest update time')