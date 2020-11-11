from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordChangeDoneView
)

app_name = 'accounts'

urlpatterns = [
    # Login
    path(
        'login/',
        LoginView.as_view(
            template_name='accounts/login.html'
        ),
        name='login'
    ),

    # Logout
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    # Password change
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='accounts/password_change.html'
        ),
        name='password_change'
    ),
    path(
        'password_change_done/',
        PasswordChangeDoneView.as_view(
            template_name='password_changed.html'
        ),
        name = 'password_change_done'
    ),
]
