from django.shortcuts import render, redirect, get_object_or_404
from .models import BugReport
from .forms import BugReportForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework import generics
from .serializers import BugReportSerializer
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .models import UserProfile


def home(request):
    profile = None
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
    return render(request, 'home.html', {'profile': profile})

@login_required
def dashboard(request):
    # Count bugs by status
    bugs = BugReport.objects.all()
    opened_bugs = bugs.filter(status='Open').count()
    resolved_bugs = bugs.filter(status='Resolved').count()
    total_bugs = [opened_bugs, resolved_bugs]

    # Count bugs by severity
    low_severity = bugs.filter(severity='Low').count()
    medium_severity = bugs.filter(severity='Medium').count()
    high_severity = bugs.filter(severity='High').count()
    critical_severity = bugs.filter(severity='Critical').count()
    severity_counts = [low_severity, medium_severity, high_severity, critical_severity]

    # Count bugs by assignee
    name = request.user
    user_assigned_bugs = bugs.filter(assigned_to=name).count()
    all_bugs = bugs.count()
    remaining_bugs = all_bugs - user_assigned_bugs
    assigned_counts = [user_assigned_bugs, remaining_bugs]

    context = {
        'total_bugs': total_bugs,
        'severity_counts': severity_counts,
        'assigned_counts': assigned_counts,
    }
    return render(request, 'dashboard.html', context)


@login_required
def bug_list(request):
    status_filter = request.GET.get('status')
    severity_filter = request.GET.get('severity')

    if request.user.userprofile.role == 'Reporter':
        bugs = BugReport.objects.filter(reporter=request.user)
    else:
        bugs = BugReport.objects.all()

    if status_filter:
        bugs = bugs.filter(status=status_filter)
    if severity_filter:
        bugs = bugs.filter(severity=severity_filter)

    return render(request, 'bugs/bug_list.html', {
        'bugs': bugs,
        'status_filter': status_filter,
        'severity_filter': severity_filter,
    })


@login_required
def bug_create(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.reporter = request.user
            bug.save()
            return redirect('bug_list')
    else:
        form = BugReportForm()
    return render(request, 'bugs/bug_form.html', {'form': form})

@login_required
def bug_update(request, pk):
    bug = get_object_or_404(BugReport, pk=pk)
    form = BugReportForm(request.POST or None, instance=bug)
    if form.is_valid():
        form.save()
        return redirect('bug_list')
    return render(request, 'bugs/bug_form.html', {'form': form})


class BugDeleteView(LoginRequiredMixin, DeleteView):
    model = BugReport
    template_name = 'bugs/bug_confirm_delete.html'
    success_url = reverse_lazy('bug_list')  # Adjust if your list view is named differently


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']
            UserProfile.objects.get_or_create(user=user, defaults={'role': role})
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class BugListAPI(generics.ListAPIView):
    queryset = BugReport.objects.all()
    serializer_class = BugReportSerializer

class BugDetailAPI(generics.RetrieveAPIView):
    queryset = BugReport.objects.all()
    serializer_class = BugReportSerializer