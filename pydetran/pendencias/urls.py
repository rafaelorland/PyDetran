from django.urls import path
from .views import homePagePendencias, inserirpendencia, consultarpendencia, mostrar_pendencia, excluir_pendencia, historico

urlpatterns = [
    path('', homePagePendencias, name = 'homepagependecias'),
    path('excluirpendencia/<int:pendencia_id>/', excluir_pendencia, name = 'excluirpendencia'),
    path('consultarpendencia/', consultarpendencia, name = 'consultarpendencia'),
    path('historico/', historico, name = 'historico' ),
    path('pendencia/<int:pendencia_id>/', mostrar_pendencia, name='mostrar_pendencia'),
    path('inserirpendencia/' , inserirpendencia, name = 'inserirpendencia'),
]
