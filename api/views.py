from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



from django.shortcuts import render
from rest_framework import generics
from .models import Events,Coordinators,Posters
from .serializers import EventsSerializer,CoordinatorSerializer,PosterSerializer
# Create your views here.

class EventView(generics.ListCreateAPIView):
    queryset= Events.objects.all()
    serializer_class=EventsSerializer

class CoordinatorView(generics.ListCreateAPIView):
    queryset= Coordinators.objects.all()
    serializer_class=CoordinatorSerializer

class PosterView(generics.ListCreateAPIView):
    queryset= Posters.objects.all()
    serializer_class=PosterSerializer

