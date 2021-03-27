from rest_framework import serializers

from apps.car.models import CarGeneration


class CarGenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGeneration
        fields = '__all__'
