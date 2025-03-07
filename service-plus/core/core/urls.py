
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from home import views


urlpatterns = [
    path('', views.home_view),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
