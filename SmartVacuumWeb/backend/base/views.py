from django.shortcuts import render
from django.http import JsonResponse

from .models import Sensor
from .serializers import SensorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST','PUT'])
def getRoutes(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def getSensors(request):
    sensors = Sensor.objects.all() # Query Set
    serializer = SensorSerializer(sensors, many= True)
    return Response(serializer.data)

@api_view(['GET','PUT'])
def getSensor(request, pk):
    sensor = Sensor.objects.get(_id= pk)
    if request.method == 'PUT':
        new_value = request.data["value"]
        sensor.value= float(new_value)
        sensor.save()
        return Response({"message": "Updated", "value": new_value}) 
    serializer = SensorSerializer(sensor, many = False)
    return Response(serializer.data)