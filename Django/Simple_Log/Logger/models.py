from django.db import models

class LOG(models.Model):
    USERNAME = models.CharField(max_length=16)
    IP_ADDR = models.GenericIPAddressField()
    URL = models.URLField(null=True)
    FUNC_NAME = models.CharField(max_length=64)
    DATE = models.DateTimeField()
    logmanager = models.Manager()
