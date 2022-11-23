from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from cars.views import pageNotFound


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls', namespace='cars'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


handler404 = pageNotFound
