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
from django.urls import path, include
from tasks.views import home, completed, remaining, add_task, delete_task, task_detail, toggle_complete, remove_task, prueba

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('tasks', home, name='home'),
    path('completed', completed, name='completed'),
    path('remaining', remaining, name='remaining'),
    path('add_task', add_task, name='add_task'),
    path('delete_task/<str:task_id>', delete_task, name='delete_task'),
    path('detail/<str:task_id>', task_detail, name='detail'),
    path('toggle_complete/<str:task_id>',
         toggle_complete, name='toggle_complete'),
    path('remove_task/<str:task_id>', remove_task, name='remove_task'),
    path('prueba', prueba, name='prueba')
]
