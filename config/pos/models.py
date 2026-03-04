from django.db import models
from merchants.models import Merchant
from django.conf import settings


class POS(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='pos_list')
    MID = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='merchant_id')
    TID = models.CharField(max_length=255, unique = True)
    SNO = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    google_map_link = models.URLField(blank=True)
    status = models.CharField(max_length=20, default='ACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='created_pos',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pos_name} - {self.merchant.name}"