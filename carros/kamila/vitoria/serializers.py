from rest_framework import serializers
from .models import Carro
# classe do meu carro - basicamente um convertor de modelo
class CarroSerializer(serializers.ModelSerializer):#converte json para o meu modelo ou o inverso
    class Meta:
        model = Carro
        fields = '__all__'