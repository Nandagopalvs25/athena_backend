from .models import Events,Coordinators,Posters
from rest_framework import serializers



class PosterSerializer(serializers.ModelSerializer):
  class Meta:
   model=Posters
   fields=['link','event']

class CoordinatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Coordinators
        fields=['cord_num','cord_name','event']


class EventsSerializer(serializers.ModelSerializer):
    cords = CoordinatorSerializer(many=True,read_only=True)
    posters= PosterSerializer(many=True,read_only=True)


    class Meta:
        model=Events
        fields=['id','name','details','date','price','cords','posters']

