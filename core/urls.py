from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views


urlpatterns = [
    path('home/', include('home.urls')),
    path('', include('login.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('servico/', include('servicos.urls', namespace='servicos')),

    # API URLS
    path('api/v1/home/', include('home.api.urls'))
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)