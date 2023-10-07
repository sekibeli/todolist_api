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
    API endpoint that allows todos to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at')  #Abruf der todos aus der Datenbank sortiert nach created_at
    serializer_class = TodoSerializer  # Anweisung an DRF den selbst geschriebenen TodoSerializer zu verwenden
    permission_classes = []  #permissions.IsAuthenticated  # aktuell so keine permission notwendig, um diese Klasse zu benutzen


    def create(self, request):
        todo = Todo.objects.create(title= request.data.get('title', ''), #ungewöhnlich die create-Funktion zu überschreiben, da Django das eigentlich selber machen kann
                                  description= request.data.get('description', ''), #Ein neues todo Objekt wird erstellt
                                  user= request.user,
                                )
        serialized_obj = serializers.serialize('json', [todo, ]) #das todo wird in ein JSON-Format serialisiert
        return HttpResponse(serialized_obj, content_type='application/json') #Die HTTP Antwort gibt das serialisierte Todo zur weiteren Verwendung zurück
      
      
   # ---> von chatGPT vorgeschlagener Code für die obige Funktion, die das DRF wirklich benutzt:   
# from rest_framework import viewsets, permissions
# from .models import Todo
# from .serializers import TodoSerializer

# class TodoViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows todos to be viewed or edited.
#     """
#     queryset = Todo.objects.all().order_by('-created_at')
#     serializer_class = TodoSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
