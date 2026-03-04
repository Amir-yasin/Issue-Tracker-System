from django.db import models
from django.conf import settings


class Merchant(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    MID = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='created_merchants',on_delete=models.CASCADE)


    def __str__(self):
        return self.name