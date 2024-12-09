from django.db import models

class usuario(models.Model): 
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)   
    cpf = models.CharField(max_length=20)
    nasc = models.DateField()
    telefone = models.CharField(max_length=30)

    def  __str__(self):
        return self.nome
    
class carro(models.Model): 
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    ano = models.CharField(max_length=4)

    def __str__(self):
        return self.modelo
    
class Nivel (models.Model): 
    CATEGORIA = (
        ('S.B','Seguro contra batida'),
        ('S.F','Seguro contra furto'),
        ('S.R','seguro reboque'),
        ('S.C','Seguro Completo'),
    )
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    carro = models.ForeignKey(carro, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=5, choices= CATEGORIA, blank=False, default="SG")





    




