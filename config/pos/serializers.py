from rest_framework import serializers
from .models import POS
from merchants.models import Merchant


class POSSerializer(serializers.ModelSerializer):

    MID = serializers.SlugRelatedField(     
        queryset=Merchant.objects.all(),
        slug_field='MID'     # Telling Django to look up the user by 'username' instead of 'id'

    )

    class Meta:
        model = POS
        fields = '__all__'