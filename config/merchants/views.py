from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Merchant
from .serializers import MerchantSerializer
from users.permissions import IsAdmin


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = [IsAuthenticated, IsAdmin]