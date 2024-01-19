
from django.contrib import admin
from django.urls import path
from apps.views import funcao_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', funcao_login)
    
]
