from django.conf import settings
from rest_framework.response import Response
from rest_framework import status 

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers


from .serializers import TodoSerializer
from .models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = []  #permissions.IsAuthenticated


    def create(self, request):
        todo = Todo.objects.create(title= request.data.get('title', ''), 
                                  description= request.data.get('description', ''),
                                  user= request.user,
                                )
        serialized_obj = serializers.serialize('json', [todo, ])
        return HttpResponse(serialized_obj, content_type='application/json')