from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from apps.base.views import base_view
from apps.pages.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base_view, name='base_view'),

    path('', index, name='index'),  # Rota para a página inicial
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)