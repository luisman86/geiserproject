
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ClienteViewSet, DireccionViewSet, UserViewSet, StatusViewSet, OrigenViewSet, ServicioViewSet

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('direcciones', DireccionViewSet)
router.register('users', UserViewSet)
router.register('status', StatusViewSet)
router.register('origenes', OrigenViewSet)
router.register('servicios', ServicioViewSet)

urlpatterns = [
    path('', include(router.urls))
]
