from django.shortcuts import render
from django.http import JsonResponse
from locadora.serializers import ususarioSerializer, carroSerializer, NivelSerializer, ListaNivelsusuarioSerializer
from rest_framework import viewsets, generics
from locadora.models import usuario, carro, Nivel
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import BasicAuthentication

class usuarioViewSet(viewsets.ModelViewSet): 
    queryset = usuario.objects.all()
    serializer_class = ususarioSerializer

class carroViewSet(viewsets.ModelViewSet): 
    queryset = carro.objects.all()
    serializer_class = carroSerializer

class NivelViewSet(viewsets.ModelViewSet): 
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

class ListaNivelusuario(generics.ListAPIView): 
    def get_queryset(self):
        queryset = Nivel.objects.filter(usuario_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaNivelsusuarioSerializer

