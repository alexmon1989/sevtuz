from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import MyAuthenticationForm
from .views import dashboard

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='staff_office/login.html', form_class=MyAuthenticationForm),
        name='login'
    ),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
        name='password_reset'
    ),
    path('dashboard/', dashboard, name='staff_office_dashboard')
]
