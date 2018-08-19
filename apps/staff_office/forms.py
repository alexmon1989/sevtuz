from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


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
        self.fields['username'].widget.attrs = {'class': 'form-control g-color-black g-bg-white g-bg-white--focus '
                                                         'g-brd-gray-light-v4 g-brd-primary--hover rounded '
                                                         'g-py-15 g-px-15',
                                                'placeholder': 'Логин'}
        self.fields['password'].widget.attrs = {'class': 'form-control g-color-black g-bg-white g-bg-white--focus '
                                                         'g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 '
                                                         'g-px-15 mb-3',
                                                'placeholder': 'Пароль'}
