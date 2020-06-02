from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from.models import Cliente, Direccion, Status, Origen, Servicio


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    direcciones = DireccionSerializer(many=True, read_only=True, source='direccion_set')
    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'apellido_paterno', 'apellido_materno', 'direcciones')
        #extra_kwargs = {'nombre': {'required': True}}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
        #extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data)
        Token.objects.create(user=user)
        return user


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class OrigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origen
        fields = '__all__'


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'