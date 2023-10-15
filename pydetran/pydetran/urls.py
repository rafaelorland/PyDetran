from django.contrib import admin
from django.urls import path, include
from pydetran.views import homePage, user_login, user_logout

urlpatterns = [
    path('', homePage, name = 'homepage'),
    path('admin/', admin.site.urls),
    path('pendencias/', include('pendencias.urls')),
    path('login/', user_login, name = 'login'),
    path('logout/', user_logout, name = 'logout')   ,
]