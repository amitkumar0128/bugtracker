# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import BugReport
from .forms import BugReportForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'home.html')

def bug_list(request):
    status_filter = request.GET.get('status')
    severity_filter = request.GET.get('severity')

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
            form.save()
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

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
