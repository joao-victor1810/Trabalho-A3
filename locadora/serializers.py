from rest_framework import serializers
from locadora.models import usuario, carro, Nivel

class ususarioSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = usuario
        fields = '__all__'

class carroSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = carro
        fields = '__all__'    

class NivelSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Nivel 
        exclude = []

class ListaNivelsusuarioSerializer(serializers.ModelSerializer):
    carro = serializers.ReadOnlyField(source= 'carro.descriçao')
    categoria = serializers.SerializerMethodField()
    class Meta : 
        model = Nivel
        fields = ['carro', 'categoria']
    def get_categoria(self, obj): 
            return obj.get_categoria_display()
        
class ListaNivelscarroSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.ReadOnlyField(source='usuario.nome')
    class Meta : 
        model = Nivel
        fields = ['usuario_nome']