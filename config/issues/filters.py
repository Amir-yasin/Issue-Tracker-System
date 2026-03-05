import django_filters
from .models import Issue


class IssueFilter(django_filters.FilterSet):

    created_after = django_filters.DateFilter(field_name="created_at", lookup_expr='gte')
    created_before = django_filters.DateFilter(field_name="created_at", lookup_expr='lte')

    class Meta:
        model = Issue
        fields = [
            'status',
            'priority',
            'TID',
            'assigned_to',
        ]