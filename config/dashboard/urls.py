from django.urls import path
from .views import DashboardSummaryView, StatusChartView, MonthlyReportView, MerchantReportView

urlpatterns = [
    path('summary/', DashboardSummaryView.as_view()),
    path('status-chart/', StatusChartView.as_view()),
    path('monthly-report/', MonthlyReportView.as_view()),
    path('merchant-report/', MerchantReportView.as_view()),
]