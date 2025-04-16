from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bug_list/', views.bug_list, name='bug_list'),
    path('bug_create/', views.bug_create, name='bug_create'),
    path('bug_update/<int:pk>/', views.bug_update, name='bug_update'),
    path('register/', views.register_view, name='register'),
]
