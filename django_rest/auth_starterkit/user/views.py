from rest_framework.views import APIView
from user.backend import authenticate, login, loginJWT, logout
from django.http import JsonResponse, HttpResponse
import json
from user.models import User
from user.serializers import UserSerializer


class Login(APIView):
    def post(self, request):
        public_address = request.data.get('public_address', '')
        signature = request.data.get('signature', '')
        user = authenticate(public_address=public_address, signature=signature)
        if not user:
            return HttpResponse('Unauthorized', status=401)
        login(request, user)
        return JsonResponse(UserSerializer(user).data)


class LoginJWT(APIView):
    def post(self, request):
        public_address = request.data.get('public_address', '')
        signature = request.data.get('signature', '')
        user = authenticate(public_address=public_address, signature=signature)
        if not user:
            return HttpResponse('Unauthorized', status=401)
        jwt_token = loginJWT(request, user)
        return JsonResponse({
            'user': UserSerializer(user).data,
            'token': jwt_token.decode('utf-8')
        })


class Logout(APIView):
    def get(self, request):
        logout(request)
        return HttpResponse('Success')


class Nonce(APIView):
    def get(self, request, public_address=''):
        user = User.objects.get_or_create(
            public_address=public_address.lower())[0]
        return JsonResponse({'nonce': user.nonce })


class CurrentUserView(APIView):
    def get(self, request):
        if request.is_logged_in:
            return JsonResponse(UserSerializer(request.current_user).data)
        return HttpResponse('Unauthorized', status=401)


class UserView(APIView):
    def put(self, request, public_address):
        if request.is_logged_in and request.current_user.public_address == public_address.lower():
            user = request.current_user
            user.username = request.data.get('username', '')
            user.save()
            return JsonResponse(UserSerializer(user).data)
        return HttpResponse('Unauthorized', status=401)
