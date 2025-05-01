from django.db import models

# Create your models here.

from django.contrib.auth.models import User

def get_default_reporter():
    default_user = User.objects.first()  
    return default_user.id if default_user else None

class BugReport(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Open')
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    project = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_reporter, related_name='reported_bugs') 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.status}] {self.title}"

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Reporter', 'Reporter'),
        ('Developer', 'Developer'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"