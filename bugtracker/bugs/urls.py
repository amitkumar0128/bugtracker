from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('bug_list/', views.bug_list, name='bug_list'),
    path('bug_create/', views.bug_create, name='bug_create'),
    path('bug_update/<int:pk>/', views.bug_update, name='bug_update'),
    path('register/', views.register, name='register'),
    path('api/bugs/', views.BugListAPI.as_view(), name='api_bugs'),
    path('api/bugs/<int:pk>/', views.BugDetailAPI.as_view(), name='api_bug_detail'),
    path('bug/<int:pk>/delete/', views.BugDeleteView.as_view(), name='bug_delete'),
]
