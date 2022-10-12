
from rest_framework import serializers
from .models import Sensor,Status

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'



class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'