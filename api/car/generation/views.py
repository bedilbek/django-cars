from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.car.generation.serializers import CarGenerationSerializer
from apps.car.models import CarGeneration


class CarGenerationCreateListView(ListCreateAPIView):
    queryset = CarGeneration.objects.all()
    serializer_class = CarGenerationSerializer


class CarGenerationRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = CarGeneration.objects.all()
    serializer_class = CarGenerationSerializer
