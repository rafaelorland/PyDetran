from django.urls import path
from .views import homePagePendencias, inserirpendencia

urlpatterns = [
    path('', homePagePendencias, name = 'homepagependecias'),
    path('inserirpendencia/' , inserirpendencia, name = 'inserirpendencia')
]
