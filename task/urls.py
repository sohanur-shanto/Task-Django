from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('', include('task1.urls', namespace='task1')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)