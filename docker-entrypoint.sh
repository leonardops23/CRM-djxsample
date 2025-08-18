#!/bin/bash

# Script de entrada para Docker
set -e

# Función para esperar a que la base de datos esté lista
wait_for_db() {
    echo "Esperando a que la base de datos esté lista..."
    while ! python manage.py check --database default 2>&1; do
        sleep 1
    done
    echo "Base de datos lista!"
}

# Función para ejecutar migraciones
run_migrations() {
    echo "Ejecutando migraciones..."
    python manage.py makemigrations --noinput
    python manage.py migrate --noinput
    echo "Migraciones completadas!"
}

# Función para crear superusuario si no existe
create_superuser() {
    echo "Verificando superusuario..."
    if ! python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists()" 2>/dev/null; then
        echo "Creando superusuario 'admin'..."
        python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superusuario creado: admin/admin123')
"
    else
        echo "Superusuario ya existe!"
    fi
}

# Función para recolectar archivos estáticos
collect_static() {
    echo "Recolectando archivos estáticos..."
    python manage.py collectstatic --noinput
    echo "Archivos estáticos recolectados!"
}

# Función principal
main() {
    echo "Iniciando aplicación Django CRM..."
    
    # Cambiar al directorio de la aplicación
    cd /app
    
    # Esperar a que la base de datos esté lista
    wait_for_db
    
    # Ejecutar migraciones
    run_migrations
    
    # Crear superusuario si es necesario
    create_superuser
    
    # Recolectar archivos estáticos
    collect_static
    
    echo "Aplicación lista para ejecutarse!"
    
    # Ejecutar el comando principal
    exec "$@"
}

# Ejecutar función principal con todos los argumentos
main "$@"
