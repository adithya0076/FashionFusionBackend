from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from api import models as model
from api import serializer as ser
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# Create your views here.
class UserLoginView(APIView):
    def post(self, request):
        serializer = ser.UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user:
            
            return Response({'status':'login successfull'})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)
        
class UserRegistrationView(APIView):
    def post(self, request):
        print(request.data)
        serializer = ser.UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'Registration successfull'})
        return Response({'status': 'Registration failed: Unknown error'})
    
