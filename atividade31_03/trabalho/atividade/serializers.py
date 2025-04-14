from rest_framework import serializers
from .models import UsuarioDS16
#esse documento serve para converter seu modelo em json e ao contrário também
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDS16
        fields = '__all__'