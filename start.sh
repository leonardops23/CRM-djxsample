#!/bin/bash

# Script de inicio rápido para CRM Django con Docker
set -e

echo "🚀 Iniciando CRM Django con Docker..."

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para mostrar mensajes
print_message() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE} $1${NC}"
    echo -e "${BLUE}================================${NC}"
}

# Verificar si Docker está instalado
check_docker() {
    if ! command -v docker &> /dev/null; then
        print_error "Docker no está instalado. Por favor instala Docker primero."
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose no está instalado. Por favor instala Docker Compose primero."
        exit 1
    fi
    
    print_message "Docker y Docker Compose están instalados."
}

# Verificar si el archivo .env existe
check_env() {
    if [ ! -f .env ]; then
        print_warning "Archivo .env no encontrado. Creando desde env.example..."
        if [ -f env.example ]; then
            cp env.example .env
            print_message "Archivo .env creado. Por favor revisa y ajusta las variables."
        else
            print_error "Archivo env.example no encontrado."
            exit 1
        fi
    else
        print_message "Archivo .env encontrado."
    fi
}

# Función para construir las imágenes
build_images() {
    print_header "Construyendo imágenes Docker"
    docker-compose build
    print_message "Imágenes construidas exitosamente."
}

# Función para levantar servicios
start_services() {
    print_header "Levantando servicios"
    docker-compose up -d
    print_message "Servicios iniciados."
}

# Función para esperar a que los servicios estén listos
wait_for_services() {
    print_header "Esperando a que los servicios estén listos"
    
    # Esperar a que PostgreSQL esté listo
    print_message "Esperando a que PostgreSQL esté listo..."
    while ! docker-compose exec -T db pg_isready -U crm_user -d crm_db > /dev/null 2>&1; do
        sleep 2
    done
    print_message "PostgreSQL está listo."
    
    # Esperar a que Redis esté listo
    print_message "Esperando a que Redis esté listo..."
    while ! docker-compose exec -T redis redis-cli ping > /dev/null 2>&1; do
        sleep 2
    done
    print_message "Redis está listo."
    
    # Esperar a que Django esté listo
    print_message "Esperando a que Django esté listo..."
    while ! curl -s http://localhost:8000/ > /dev/null 2>&1; do
        sleep 3
    done
    print_message "Django está listo."
}

# Función para ejecutar migraciones
run_migrations() {
    print_header "Ejecutando migraciones"
    docker-compose exec -T web python manage.py migrate
    print_message "Migraciones completadas."
}

# Función para crear superusuario
create_superuser() {
    print_header "Verificando superusuario"
    if ! docker-compose exec -T web python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists()" 2>/dev/null; then
        print_message "Creando superusuario 'admin'..."
        docker-compose exec -T web python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superusuario creado: admin/admin123')
"
        print_message "Superusuario creado: admin/admin123"
    else
        print_message "Superusuario ya existe."
    fi
}

# Función para mostrar información
show_info() {
    print_header "Información de la Aplicación"
    echo -e "${GREEN}✅ Aplicación web:${NC} http://localhost:8000"
    echo -e "${GREEN}✅ Admin Django:${NC} http://localhost:8000/admin"
    echo -e "${GREEN}✅ Base de datos:${NC} localhost:5432"
    echo -e "${GREEN}✅ Redis:${NC} localhost:6379"
    echo ""
    echo -e "${YELLOW}🔑 Credenciales por defecto:${NC}"
    echo -e "   Usuario: admin"
    echo -e "   Contraseña: admin123"
    echo ""
    echo -e "${BLUE}📋 Comandos útiles:${NC}"
    echo -e "   make help          - Mostrar todos los comandos"
    echo -e "   make logs          - Ver logs en tiempo real"
    echo -e "   make status        - Estado de los servicios"
    echo -e "   make down          - Detener servicios"
    echo -e "   make shell         - Acceder al contenedor"
}

# Función principal
main() {
    print_header "CRM Django - Inicio con Docker"
    
    # Verificaciones
    check_docker
    check_env
    
    # Construir y levantar
    build_images
    start_services
    
    # Esperar servicios
    wait_for_services
    
    # Configuración inicial
    run_migrations
    create_superuser
    
    # Mostrar información
    show_info
    
    print_header "¡Aplicación iniciada exitosamente!"
    print_message "Puedes acceder a la aplicación en: http://localhost:8000"
}

# Ejecutar función principal
main "$@"
