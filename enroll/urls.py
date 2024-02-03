
from django.urls import path,include
from enroll.views import EnrollListView



urlpatterns=[
     path('enroll_now/',EnrollListView.as_view(),name='course'),
     
]