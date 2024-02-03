
from django.urls import path,include
from user.views import UserRegisterView,UserLoginView,GetData,LogoutView,ChangePasswordView,SendPasswordResetLinkView,ResestPasswordView


urlpatterns = [
   path('register/',UserRegisterView.as_view(),name='register'),
   path('login/',UserLoginView.as_view(),name='login'),
   path('getdata/',GetData.as_view(),name='getdata'),
   path('logout/',LogoutView.as_view(),name='logout'),
   path('changepassword/',ChangePasswordView.as_view(),name='changepassword'),
   path('reset_password_user/',SendPasswordResetLinkView.as_view(),name='reset_password_user'),
   path('reset_password/<uid>/<token>/',ResestPasswordView.as_view(),name='reset_password'),
]
