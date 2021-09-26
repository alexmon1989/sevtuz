from django.contrib.auth.models import User
from django.shortcuts import redirect


class StaffOfficeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if 'forum' in request.path:
            try:
                request.user.person
            except AttributeError:
                return redirect('/staff-office/login/')
            except User.person.RelatedObjectDoesNotExist:
                return redirect('/staff-office/login/')
        response = self.get_response(request)
        return response
