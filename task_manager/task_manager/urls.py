"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from tasks.views import home, add_task, delete_task, edit_task, toggle_complete, remove_task, register, LoginView, custom_logout, calendar_view, mark_all_notifications_read, mark_notification_read, delete_notification, delete_all_notifications, view_task, landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', landing, name='landing'),
    path('tasks/', home, name='home'),
    path('add_task/', add_task, name='add_task'),
    path('delete_task/<str:task_id>', delete_task, name='delete_task'),
    path('toggle_complete/<str:task_id>',
         toggle_complete, name='toggle_complete'),
    path('remove_task/<str:task_id>', remove_task, name='remove_task'),
    path('login', LoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', register, name='register'),
    path('calendar/', calendar_view, name='calendar'),
    path('api/notifications/<int:notification_id>/read/',
         mark_notification_read, name='mark_notification_read'),
    path('api/notifications/mark-all-read/',
         mark_all_notifications_read, name='mark_all_notifications_read'),
    path('api/notifications/<int:notification_id>/delete/',
         delete_notification, name='delete_notification'),
    path('api/notifications/delete-all/', delete_all_notifications,
         name='delete_all_notifications'),
    path('task/<str:task_id>/', view_task, name='view_task'),
    path('task/<str:task_id>/edit/', edit_task, name='task_detail'),

]
