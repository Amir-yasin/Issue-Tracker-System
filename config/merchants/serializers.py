from rest_framework import serializers
from .models import Merchant


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'
        read_only_fields = ['created_by', 'status']