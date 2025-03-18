from rest_framework import serializers
from .models import Carro
# classe do meu carro
class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'