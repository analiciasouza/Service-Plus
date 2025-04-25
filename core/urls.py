from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views


urlpatterns = [
    path('home/', views.home_view , name='home'),
    path('', include('login.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('servico/', include('servicos.urls', namespace='servicos')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)