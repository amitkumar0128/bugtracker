from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .models import BugReport

class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'status', 'severity', 'project', 'assigned_to']

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (                    # Can define it as global variable in models.py to avoid redundancy DRY
        ('Reporter', 'Reporter'),
        ('Developer', 'Developer'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']