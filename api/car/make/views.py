from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.car.make.serializers import CarMakeSerializer
from apps.car.models import CarMake


class CarMakeCreateListView(ListCreateAPIView):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer


class CarMakeRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer
