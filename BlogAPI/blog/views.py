from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework import generics, permissions

# Create your views here.

class UserCreateAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDataAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserOneDataAPI(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateAPI(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdatePartialAPI(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDeleteAPI(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostCreateAPI(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDataAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostOneDataAPI(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdateAPI(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdatePartialAPI(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDeleteAPI(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LikeCreateAPI(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDataAPI(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeOneDataAPI(generics.RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeUpdateAPI(generics.UpdateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeUpdatePartialAPI(generics.RetrieveUpdateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDeleteAPI(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

