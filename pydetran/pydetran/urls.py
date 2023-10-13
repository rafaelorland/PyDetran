from django.contrib import admin
from django.urls import path, include
from pydetran.views import homePage

urlpatterns = [
    path('', homePage, name= 'homepage'),
    path('admin/', admin.site.urls),
    path('pendencias/', include('pendencias.urls'))
    
]
