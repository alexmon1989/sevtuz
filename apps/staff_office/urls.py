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
        'password-reset/',
        auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
        name='password_reset'
    ),
    path('calendar/', calendar, name='staff_office_calendar'),
    path('office/', office, name='staff_office_office'),
    path('forum/', include('pybb.urls', namespace='pybb')),
    path('profile/', profile, name='staff_office_profile'),
]
