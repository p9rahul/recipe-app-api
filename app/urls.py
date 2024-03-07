#For Swagger
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #For Swagger setup
    path('api/schema/',SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
    # Redoc view to see more details
    path('api/docs/details/', SpectacularRedocView.as_view(url_name='api-schema'), name='redoc'),
    path('api/user/', include('user.urls')),
    path('api/recipe/', include('recipe.urls')),
    path('api/emp/', include('Employee.urls')),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
