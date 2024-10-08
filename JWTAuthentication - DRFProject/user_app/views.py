from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegistrationSerializer
# from . import models


# Create your views here.
@api_view(['POST',])
def logout_view(request):
    
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST',])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = 'Registration Successful!'
            data['username'] = account.username
            data['email'] = account.email
            
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            
        else:
            data = serializer.errors
            
        return Response(data)
        