from django.contrib import admin
from django.urls import path, include

from BlackFriday.swagger import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('', include('ecommerce.urls')),
    path('', include('django_prometheus.urls')),
]
