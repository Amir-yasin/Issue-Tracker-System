from django.db import models
from django.conf import settings
from merchants.models import Merchant
from pos.models import POS
from django.db import transaction

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
    MID = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='merchant_i')
    TID = models.ForeignKey(POS,  on_delete=models.CASCADE, related_name='terminal_id')
    SNO = models.ForeignKey(POS, on_delete=models.CASCADE, related_name='serial_number')
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='merchant_name')

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
    ticket_number = models.BigIntegerField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.ticket_number:
            with transaction.atomic():
                last_issue = Issue.objects.select_for_update().order_by('-id').first()
                if last_issue and last_issue.ticket_number:
                    self.ticket_number = last_issue.ticket_number + 1
                else:
                    self.ticket_number = 1000
        super().save(*args, **kwargs)