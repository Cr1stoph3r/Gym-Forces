from .models import galeria, contacto
from rest_framework import serializers


class GaleriaSerializer(serializers.ModelSerializer):
    deporte = serializers.CharField(required=True)
    imagen = serializers.ImageField(required=True)
    class Meta:
        model = galeria
        fields = '__all__'
