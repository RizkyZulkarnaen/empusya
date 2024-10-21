from django.urls import path
from . import views
from .forms import CustomPasswordResetForm
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('password-reset/', 
        PasswordResetView.as_view(
            template_name='authentication/forgot-password/password_reset.html',
            form_class=CustomPasswordResetForm,
            html_email_template_name='authentication/forgot-password/password_reset_email.html'
        ),
        name='password-reset'
    ),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='authentication/forgot-password/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='authentication/forgot-password/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='authentication/forgot-password/password_reset_complete.html'),name='password_reset_complete'),
]