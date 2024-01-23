"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from user.views import UserManage,EducationManage,ManageExperiance,ManageSkills
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserManage.as_view()),
    path('user/<int:id>/', UserManage.as_view()),
    path('education/',EducationManage.as_view()),
    path('education/<int:id>/',EducationManage.as_view()),
    path('experience/', ManageExperiance.as_view()),
    path('experience/<int:id>/', ManageExperiance.as_view()),
    path('skill/', ManageSkills.as_view()),
    path('skill/<int:id>/', ManageSkills.as_view()),
]