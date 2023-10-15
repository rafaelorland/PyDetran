from django.contrib import admin
from django.urls import path, include
from pydetran.views import homePage, user_login

urlpatterns = [
    path('', homePage, name= 'homepage'),
    path('admin/', admin.site.urls),
    path('pendencias/', include('pendencias.urls')),
    path('login/', user_login, name='login')
    
]
