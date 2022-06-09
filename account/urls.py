
from django.urls import path
from .views import *

app_name = 'account'
urlpatterns = [
    path('login/',
         MyLoginView.as_view(),
         name='login'),
    path('logout/',
         MyLogoutView.as_view(),
         name='logout'),
    path('password-change/',
         MyPasswordChangeView.as_view(),
         name='password_change'),
    path('password-change-done/',
         MyPasswordChageDoneView.as_view(),
         name='password_change_done'),
    path('password-reset/',
         MyPasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset/done/',
         MyPasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         MyPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         MyPasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('register/',
         CreateUser.as_view(),
         name='create_account'),
    path('profile/',
         UserDetailView.as_view(),
         name='edit_profile')
]
