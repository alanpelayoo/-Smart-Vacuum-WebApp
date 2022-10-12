
from .models import Sensor, Status
from .serializers import SensorSerializer, StatusSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    return Response({"message": "Hello, your connected to the API!"})

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

@api_view(['GET'])
def getStatus(request):
    status = Status.objects.get(id= 1)
    serializer = StatusSerializer(status, many= False)
    return Response(serializer.data)