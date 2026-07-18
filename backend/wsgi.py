"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()


try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    # Cambia 'admin' y 'TuContraseñaSegura123' por los datos que tú quieras
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'expedientesuptai@gmail.com', 'expedientes1')
        print("¡Superusuario creado con éxito en Render!")
except Exception as e:
    print(f"Error al intentar crear el superusuario: {e}")