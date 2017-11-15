from django.shortcuts import render


def home(request):
    """Отображает главную страницу сайта."""
    return render(request, 'home/index.html')
