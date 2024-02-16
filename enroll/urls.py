from django.urls import path,include
from enroll.views import EnrollListView,CreateOrderAPIView

urlpatterns=[
     path('enroll_now/',EnrollListView.as_view(),name='course'),
      path('create_order/',CreateOrderAPIView.as_view(),name='create_order'),
]