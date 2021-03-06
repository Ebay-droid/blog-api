from django.contrib.auth.models import User
from Api import serializers
from rest_framework import generics, permissions
from Api.models import Post
from Api.permissions import IsOwnerOrReadOnly

# Create your views here.


class UserList(generics.ListAPIView):
    queryset =  User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset =User.objects.all()
    serializer_class = serializers.UserSerializer  


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serialiazer):
        serialiazer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer  
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
                           