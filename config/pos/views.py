from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import POS
from .serializers import POSSerializer


class POSViewSet(viewsets.ModelViewSet):
    queryset = POS.objects.all()
    serializer_class = POSSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)