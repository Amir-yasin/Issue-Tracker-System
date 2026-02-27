from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'ADMIN':
            return Issue.objects.all()

        elif user.role == 'SUPPORT':
            return Issue.objects.filter(assigned_to=user)

        elif user.role == 'MERCHANT':
            return Issue.objects.filter(created_by=user)

        return Issue.objects.none()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)