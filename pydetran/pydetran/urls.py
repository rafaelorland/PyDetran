from django.contrib import admin
from django.urls import path, include
from pydetran.views import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name= 'homepage'),
    path('consulta/', include('consult.urls'))
]
