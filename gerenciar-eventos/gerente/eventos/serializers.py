from rest_framework import serializers
from .models import Postagem
#esse documento serve para converter seu modelo em json e ao contrário também
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = '__all__'