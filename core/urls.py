from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home_view),
    path('admin/', admin.site.urls),
    path('servico/', include(('servicos.urls', 'servicos'), namespace="servicos")),
] 