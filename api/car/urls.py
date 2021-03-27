from django.urls import path

from api.car.generation.views import CarGenerationCreateListView, CarGenerationRetrieveUpdateView
from api.car.make.views import CarMakeCreateListView, CarMakeRetrieveUpdateView
from api.car.model.views import CarModelCreateListView, CarModelRetrieveUpdateView

urlpatterns = [
    path('makes/', CarMakeCreateListView.as_view(), name='car_makes_list'),
    path('makes/<int:pk>', CarMakeRetrieveUpdateView.as_view(), name='car_makes_detail'),
    path('models/', CarModelCreateListView.as_view(), name='car_models_list'),
    path('models/<int:pk>', CarModelRetrieveUpdateView.as_view(), name='car_models_detail'),
    path('generations/', CarGenerationCreateListView.as_view(), name='car_generations_list'),
    path('generations/<int:pk>', CarGenerationRetrieveUpdateView.as_view(), name='car_generations_detail'),
]
