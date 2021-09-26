from .models import Person
from django.conf import settings
from django.contrib.auth.models import User


def create_users_from_persons():
    """Создаёт пользователей на основе персон театра."""
    persons = Person.objects.all()
    for person in persons:
        user = User.objects.create_user(person.slug, '', settings.PERSON_DEFAULT_PASSWORD)
        user.save()
        person.user = user
        person.save()
