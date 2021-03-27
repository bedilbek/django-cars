from rest_framework import serializers

from apps.car.models import CarMake


class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'
