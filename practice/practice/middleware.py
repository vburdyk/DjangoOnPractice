from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated or request.path == '/auth/' or request.path == '/auth/login' or request.path == '/admin' or request.path == '/signup':
            print('AuthUSer')
            return response
        print('Redirected')
        return redirect('/auth/')

