from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from django.db.models.functions import TruncMonth
from issues.models import Issue

#### DASHBOARD SUMMARY API
class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self, request):
        user = request.user

        if user.role == 'ADMIN':
            return Issue.objects.all()
        elif user.role == 'IT_TEAM':
            return Issue.objects.filter(assigned_to=user)
        elif user.role == 'SUPPORT':
            return Issue.objects.filter(created_by=user)
        return Issue.objects.none()

    def get(self, request):
        queryset = self.get_queryset(request)

        data = {
            "total_issues": queryset.count(),
            "Pending": queryset.filter(status='PENDING').count(),
            "In_progress": queryset.filter(status='IN_PROGRESS').count(),
            "resolved": queryset.filter(status='FIXED').count(),
            "Closed": queryset.filter(status='REJECTED').count(),
        }

        return Response(data)
    
    ##### STATUS CHART API (Pie Chart Data)
class StatusChartView(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self, request):
        user = request.user

        if user.role == 'ADMIN':
            return Issue.objects.all()
        elif user.role == 'IT_TEAM':
            return Issue.objects.filter(assigned_to=user)
        elif user.role == 'SUPPORT':
            return Issue.objects.filter(created_by=user)
        return Issue.objects.none()

    def get(self, request):
        queryset = self.get_queryset(request)

        data = (
            queryset
            .values('status')
            .annotate(count=Count('id'))
            .order_by('status')
        )

        return Response(data)
    
    #### MONTHLY REPORT API
class MonthlyReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self, request):
        user = request.user

        if user.role == 'ADMIN':
            return Issue.objects.all()
        elif user.role == 'IT_TEAM':
            return Issue.objects.filter(assigned_to=user)
        elif user.role == 'SUPPORT':
            return Issue.objects.filter(created_by=user)
        return Issue.objects.none()

    def get(self, request):
        queryset = self.get_queryset(request)

        data = (
            queryset
            .annotate(month=TruncMonth('created_at'))
            .values('month')
            .annotate(count=Count('id'))
            .order_by('month')
        )

        return Response(data)
    
    #### MERCHANT-WISE REPORT
class MerchantReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self, request):
        user = request.user

        if user.role == 'ADMIN':
            return Issue.objects.all()
        elif user.role == 'IT_TEAM':
            return Issue.objects.filter(assigned_to=user)
        elif user.role == 'SUPPORT':
            return Issue.objects.filter(created_by=user)
        return Issue.objects.none()

    def get(self, request):
        queryset = self.get_queryset(request)

        data = (
            queryset
            .values('merchant__name')
            .annotate(count=Count('id'))
            .order_by('-count')
        )

        return Response(data)