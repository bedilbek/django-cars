from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'))),
    path(
        'api/openapi/',
        get_schema_view(
            title='REST API',
            description='REST API Description',
            version='0.0.1',
            urlconf='api.urls',
            url='/api/',
        ),
        name='openapi-schema'
    ),
    path('api/docs/', TemplateView.as_view(
        template_name='docs/redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='docs')

]
