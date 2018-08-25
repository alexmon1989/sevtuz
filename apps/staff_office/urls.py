from django.urls import path, include
from django.contrib.auth import views as auth_views
from .forms import MyAuthenticationForm
from .views import calendar, office, profile
urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='staff_office/login.html', form_class=MyAuthenticationForm),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='/staff-office/login/'),
        name='logout'
    ),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(template_name='staff_office/change-password.html'),
        name='change_password'
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='staff_office/change-password-done.html'),
        name='password_change_done'
    ),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(template_name='staff_office/reset-password.html'),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetView.as_view(template_name='staff_office/reset-password-done.html'),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='staff_office/reset-password-confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='staff_office/reset-password-complete.html'),
        name='password_reset_complete'
    ),
    path('calendar/', calendar, name='staff_office_calendar'),
    path('office/', office, name='staff_office_office'),
    path('forum/', include('pybb.urls', namespace='pybb')),
    path('profile/', profile, name='staff_office_profile'),
]
