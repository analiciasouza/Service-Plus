from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('home/', include('home.urls')),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('servico/', include(('servicos.urls', 'servicos'), namespace="servicos")),
] 