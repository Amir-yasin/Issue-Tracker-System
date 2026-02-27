from django.db import models
from django.conf import settings
from merchants.models import Merchant


class Issue(models.Model):

    PRIORITY_CHOICES = (
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    )

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('FIXED', 'Fixed'),
        ('REJECTED', 'Rejected'),
        ('ON_HOLD', 'On Hold'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_issues',
        on_delete=models.CASCADE
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='assigned_issues',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title