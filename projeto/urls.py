
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from locadora.views import usuarioViewSet, carroViewSet, NivelViewSet, ListaNivelusuario 
from locadora import views


router = routers.DefaultRouter()
router.register('usuarios', usuarioViewSet, basename='usuarios')
router.register('carros',carroViewSet, basename= 'carros' )
router.register('nivels',NivelViewSet , basename= 'Nivels' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include (router.urls)),
    path('usuarios/<int:pk>/Nivels/', ListaNivelusuario.as_view()),

]

