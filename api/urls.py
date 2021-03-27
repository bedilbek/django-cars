from django.urls import path, include

urlpatterns = [
    path('car/', include(('api.car.urls', 'apps.car')))
]
