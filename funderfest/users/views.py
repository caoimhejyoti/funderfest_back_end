from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsUserOrReadOnly

class CustomUserList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
class CreateUser(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request, user)
            return user
        except CustomUser.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def put(self,request,pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(
            instance=user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )