from django.urls import path,include
from jobs.views import ManageJob

urlpatterns=[
    path('job/',ManageJob.as_view(),name='job')
]