from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core.views import HomeView
from dataforseo.urls import dataforseo_patterns

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('keyword-research/', include(dataforseo_patterns)),

    # Path to admin
    path('admin/', admin.site.urls, name="admin"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
