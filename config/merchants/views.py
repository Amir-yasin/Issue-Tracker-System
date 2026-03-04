from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Merchant
from .serializers import MerchantSerializer
from users.permissions import IsAdmin


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'ADMIN' or 'IT-TEAM':
            return Merchant.objects.all()

        elif user.role == 'SUPPORT':
            return Merchant.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def Delete(self, request, *args, **kwargs):
        instance = self.get_object()

        if 'id' in request.data:
            if request.user.role != 'ADMIN':
                return Response(
                    {"error": "Only ADMIN can change status"},
                    status=403
                )

        return super().update(request, *args, **kwargs)