from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory_app.urls')),  # Include app URLs here
    # Add static file serving for development
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
