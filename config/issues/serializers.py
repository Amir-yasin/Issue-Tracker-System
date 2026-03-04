from rest_framework import serializers
from .models import Issue
from merchants.models import Merchant
from pos.models import POS


class IssueSerializer(serializers.ModelSerializer):

    MID = serializers.SlugRelatedField(     
        queryset=Merchant.objects.all(),
        slug_field='MID'     # Telling Django to look up the user by 'username' instead of 'id'
    )
    TID = serializers.SlugRelatedField(     
        queryset=POS.objects.all(),
        slug_field='TID'     # Telling Django to look up the user by 'username' instead of 'id'
    )
    SNO = serializers.SlugRelatedField(     
        queryset=POS.objects.all(),
        slug_field='SNO'     # Telling Django to look up the user by 'username' instead of 'id'
    )
    # merchant = serializers.SlugRelatedField(     
    #     queryset=Merchant.objects.all(),
    #     slug_field='name'     # Telling Django to look up the user by 'username' instead of 'id'

    # )
    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ['created_by']

    