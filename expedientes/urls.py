from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudianteViewsets
from .views import registrar_usuario

router = DefaultRouter()

router.register(r'estudiantes', EstudianteViewsets, basename='estudiante')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', registrar_usuario, name='registrar_usuario')
]