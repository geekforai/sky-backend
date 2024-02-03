
from django.urls import path,include
from course.views import CourseView



urlpatterns=[
     path('course/',CourseView.as_view(),name='course'),
     path('course/<int:id>/',CourseView.as_view(),name='course'),
]