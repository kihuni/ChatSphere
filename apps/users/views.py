from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .models import User
from .serializers import UserSerializer, UserRegistrationSerializer
from .permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, 
                          status=status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                       status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            user.is_online = True
            user.save()
            return Response(UserSerializer(user).data)
        return Response({'error': 'Invalid credentials'}, 
                       status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        if request.user.is_authenticated:
            request.user.is_online = False
            request.user.save()
            logout(request)
        return Response(status=status.HTTP_200_OK)