from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User


class MyAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class': 'form-control g-color-black '
                                                         'g-brd-gray-light-v4 g-brd-primary--hover rounded '
                                                         'g-py-15 g-px-15',
                                                'placeholder': 'Логин'}
        self.fields['password'].widget.attrs = {'class': 'form-control g-color-black '
                                                         'g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 '
                                                         'g-px-15',
                                                'placeholder': 'Пароль'}

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                # Проверка является ли сотрудником театра
                try:
                    if self.user_cache.person:
                        self.confirm_login_allowed(self.user_cache)
                except User.person.RelatedObjectDoesNotExist:
                    raise forms.ValidationError(
                        self.error_messages['invalid_login'],
                        code='invalid_login',
                        params={'username': self.username_field.verbose_name},
                    )

        return self.cleaned_data
