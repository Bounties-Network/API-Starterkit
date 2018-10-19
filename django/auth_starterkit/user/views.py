from rest_framework.views import APIView
from user.backend import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
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


class Logout(APIView):
    def get(self, request):
        logout(request)
        return HttpResponse('Success')


class Nonce(APIView):
    def get(self, request, public_address=''):
        user = User.objects.get_or_create(
            public_address=public_address.lower())[0]
        return JsonResponse(
            {'nonce': user.nonce, 'has_signed_up': bool(user.email) and bool(user.name)})


class UserView(APIView):
    def get(self, request):
        if request.is_logged_in:
            setLastViewed(request, request.current_user)
            return JsonResponse(UserSerializer(request.current_user).data)
        return HttpResponse('Unauthorized', status=401)
