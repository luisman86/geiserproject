from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.permissions import  IsAuthenticated, AllowAny
from .serializers import ClienteSerializer, DireccionSerializer, UserSerializer, StatusSerializer, OrigenSerializer, ServicioSerializer
from .models import Cliente, Direccion, Status, Origen, Servicio
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from.parent import log
from django.contrib.auth import logout as do_logout
from rest_framework.views import APIView

# Create your views here.


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @action(methods=['POST'], detail=True)
    def direccion_cliente(self, request, pk=None):
        log('Entra a direccion_cliente - request.data {}'.format(request.data), 'Info')
        if 'calle' in request.data:
            cliente = Cliente.objects.get(id=pk)
            calle = request.data['calle']
            num_ext = request.data['num_ext']
            fraccionamiento = request.data['fraccionamiento']
            user = request.user
            log('User {}'.format(user), 'Info')
            try:
                direccion = Direccion.objects.get(cliente=cliente)
                direccion.calle = calle
                direccion.num_ext = num_ext
                direccion.save()

                direccion = None

                serializer = DireccionSerializer(direccion, many=False)
                response = {'message': 'direccion se actualizó', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                log('Será nueva dirección', 'Info')
                direccion = Direccion.objects.create(cliente=cliente, calle=calle, num_ext=num_ext, fraccionamiento=fraccionamiento)
                serializer = DireccionSerializer(direccion, many=False)
                response = {'message': 'direccion creada', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'por favor ingresa una calle'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        response = {'message': 'Direccion no puede ser actualizada'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class OrigenViewSet(viewsets.ModelViewSet):
    queryset = Origen.objects.all()
    serializer_class = OrigenSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)