from django.contrib import admin
from locadora.models import usuario, carro, Nivel

class usuarios(admin.ModelAdmin): 
    list_display = ('id', 'nome', 'email', 'cpf', 'nasc', 'telefone')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(usuario,usuarios)


class carros(admin.ModelAdmin): 
    list_display = ('id', 'modelo', 'marca', 'ano', )
    list_display_links = ('id', 'modelo')
    search_fields = ('modelo',)

admin.site.register(carro,carros)


class Nivels(admin.ModelAdmin): 
    list_display = ('id', 'usuario', 'carro', 'categoria')
    list_display_links = ('id',)
admin.site.register(Nivel,Nivels)
    

