from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserInfo
from .serializers import UserInfoSerializer
from django.http import Http404
import json

# Create your views here.
def home_view(request):
    context = {}
    return render(request, "home-view.html", context)

class User_List_api(APIView):
    """list all user or create a new user"""
    def get(self, request, format=None):
        user = UserInfo.objects.all()
        serializer = UserInfoSerializer(user, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
class User_Detail_api(APIView):
    """Retrieve, update or delete a user instance."""
    
    def get(self, request, account, format = None):
        try:
            user = UserInfo.objects.get(account = account)
            serializer = UserInfoSerializer(user)
            return Response(serializer.data)
        except UserInfo.DoesNotExist:
            raise Http404
        

    def post(self, request, account,format = None):
        user = UserInfo.objects.get(account)
        serializer = UserInfoSerializer(user)
        """get the account and password"""
        password = request.data.get('password')
        if serializer.is_valid():
            if user.password == password:
                return Response(request.data, status = status.HTTP_200_OK)
            else:
                return Response(status = status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, account, format = None):
        user = UserInfo.objects.get(account)
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)