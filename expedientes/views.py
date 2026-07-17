from rest_framework import viewsets, permissions
from .models import Estudiante
from .serializers import EstudianteSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class EstudianteViewsets(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializers
    permission_classes = [IsAuthenticated]
    
    def destroy(self, request, *args, **kwargs):
        # SOLO si es staff o superusuario puede eliminar
        if not request.user.is_staff and not request.user.is_superuser:
            raise PermissionDenied("No tienes permisos para eliminar expedientes.")
        return super().destroy(request, *args, **kwargs)
    
    
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        # Valida el usuario y contraseña usando el formulario nativo
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        # Obtiene o crea el token del usuario
        token, created = Token.objects.get_or_create(user=user)
        
        # AQUÍ devolvemos el token y también si es administrador (is_staff)
        return Response({
            'token': token.key,
            'is_admin': user.is_staff  # Devuelve True si es Admin, False si no
        })
        
        
        
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
@permission_classes([AllowAny]) # Permitir que se registren sin estar logueados
def registrar_usuario(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not password or not email:
        return Response({'detail': 'Todos los campos son obligatorios.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'detail': 'El nombre de usuario ya existe.'}, status=status.HTTP_400_BAD_REQUEST)

    # Creamos el usuario operativo estándar (is_staff=False por defecto)
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({'detail': 'Usuario creado exitosamente.'}, status=status.HTTP_201_CREATED)