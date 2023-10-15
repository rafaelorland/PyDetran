from django.urls import path
from .views import homePagePendencias, inserirpendencia, consultarpendencia, mostrar_pendencia

urlpatterns = [
    path('', homePagePendencias, name = 'homepagependecias'),
    path('consultarpendencia/', consultarpendencia, name = 'consultarpendencia'),
    path('pendencia/<int:pendencia_id>/', mostrar_pendencia, name='mostrar_pendencia'),
    path('inserirpendencia/' , inserirpendencia, name = 'inserirpendencia'),
]
