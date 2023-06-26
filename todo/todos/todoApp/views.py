from django.http import HttpResponse, request
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Todo
from .serializers import todoSerializer


# Create your views here.

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = todoSerializer


class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = todoSerializer

class UpdateTodo(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = todoSerializer

class RetrieveSingleTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = todoSerializer

    #
    # def get(self, request, pk, *args ,**kwargs):
    #     id = Todo.objects.get(pk=pk)
    #     serializer = todoSerializer(id)
    #     return Response(serializer.data)

    # def error(self):
    #     if request.method == 'GET':
    #         s = Todo.objects.filter(id=id)
    #         if not s:
    #             return HttpResponse("Invalid Id")


    # def error(self):
    #     s = Todo.objects.filter(id=id)
    #     if not s:
    #         return HttpResponse("Invalid Id")

class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = todoSerializer