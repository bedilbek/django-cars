from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.car.model.serializers import CarModelSerializer
from apps.car.models import CarModel


class CarModelCreateListView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CarModelRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
