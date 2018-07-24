from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import routers, serializers,viewsets

class TodoViewSet(viewsets.ModelViewSet):
	queryset=Todo.objects.all()
	serializer_class = TodoSerializer
