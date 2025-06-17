"""
URL configuration for gorevyonetimi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse
from tasks.views import task_list, create_task, toggle_task

def hello(request):
    return HttpResponse("Merhaba, Django!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('task_list/', task_list, name='task_list'),
    path('create/', create_task, name='create_task'),
    path('toggle/<int:task_id>/', toggle_task, name='toggle_task')
]
