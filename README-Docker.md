# Docker para CRM Django

Este documento describe cómo usar Docker para ejecutar la aplicación CRM Django.

## 🚀 Inicio Rápido

### 1. Construir y levantar servicios
```bash
# Construir imágenes
make build

# Levantar servicios
make up

# O para desarrollo
make dev-up
```

### 2. Acceder a la aplicación
- **Aplicación web**: http://localhost:8000
- **Admin Django**: http://localhost:8000/admin
- **Base de datos**: localhost:5432
- **Redis**: localhost:6379

### 3. Credenciales por defecto
- **Superusuario**: admin / admin123
- **Base de datos**: crm_user / crm_password

## 📁 Estructura de Archivos Docker

```
├── Dockerfile                 # Imagen base de la aplicación
├── docker-compose.yml         # Configuración principal
├── docker-compose.override.yml # Configuración para desarrollo
├── docker-compose.prod.yml    # Configuración para producción
├── nginx.conf                 # Configuración Nginx para desarrollo
├── nginx.prod.conf            # Configuración Nginx para producción
├── docker-entrypoint.sh       # Script de inicialización
├── .dockerignore              # Archivos a excluir del contexto
├── requirements.prod.txt      # Dependencias para producción
├── env.example                # Variables de entorno de ejemplo
└── Makefile                   # Comandos útiles
```

## 🛠️ Comandos Principales

### Desarrollo
```bash
make dev-up          # Levantar servicios de desarrollo
make dev-down        # Detener servicios de desarrollo
make dev-shell       # Acceder al shell del contenedor
make logs            # Ver logs en tiempo real
make status          # Estado de los servicios
```

### Base de datos
```bash
make migrate         # Ejecutar migraciones
make makemigrations  # Crear nuevas migraciones
make db-shell        # Acceder a PostgreSQL
make redis-cli       # Acceder a Redis
```

### Producción
```bash
make prod-up         # Levantar servicios de producción
make prod-down       # Detener servicios de producción
make prod-logs       # Logs de producción
```

### Utilidades
```bash
make help            # Mostrar todos los comandos
make clean           # Limpiar recursos Docker
make backup          # Crear backup de la BD
```

## 🔧 Configuración

### Variables de Entorno
Copia `env.example` a `.env` y ajusta los valores:

```bash
cp env.example .env
```

### Configuración de Base de Datos
La aplicación está configurada para usar PostgreSQL por defecto. Para cambiar a SQLite en desarrollo, modifica `docker-compose.override.yml`.

### Configuración de Nginx
- **Desarrollo**: `nginx.conf` (puerto 80)
- **Producción**: `nginx.prod.conf` (puertos 80 y 443 con SSL)

## 🐳 Servicios Docker

### 1. Web (Django)
- **Puerto**: 8000
- **Imagen**: Construida localmente
- **Volúmenes**: Código fuente, archivos estáticos y media

### 2. Base de Datos (PostgreSQL)
- **Puerto**: 5432
- **Imagen**: postgres:15
- **Volúmenes**: Datos persistentes

### 3. Cache (Redis)
- **Puerto**: 6379
- **Imagen**: redis:7-alpine
- **Uso**: Cache, sesiones, colas

### 4. Nginx (Opcional)
- **Puerto**: 80 (desarrollo) / 80,443 (producción)
- **Imagen**: nginx:alpine
- **Función**: Proxy reverso, archivos estáticos

## 🔒 Seguridad

### Variables de Entorno
- **Nunca** commits archivos `.env` con credenciales reales
- Usa `env.example` como plantilla
- Cambia todas las contraseñas por defecto

### Usuario del Contenedor
- La aplicación se ejecuta como usuario no-root (`appuser`)
- Permisos mínimos necesarios

### Headers de Seguridad
- Nginx incluye headers de seguridad básicos
- Configuración SSL para producción

## 📊 Monitoreo

### Logs
```bash
make logs            # Todos los servicios
make logs-web        # Solo aplicación web
make logs-db         # Solo base de datos
```

### Estado de Servicios
```bash
make status          # Estado de contenedores
make top             # Uso de recursos
```

### Redes y Volúmenes
```bash
make network-ls      # Listar redes
make volume-ls       # Listar volúmenes
```

## 🚨 Solución de Problemas

### Contenedor no inicia
```bash
# Ver logs detallados
make logs

# Verificar estado
make status

# Reconstruir imagen
make build
```

### Base de datos no conecta
```bash
# Verificar estado de PostgreSQL
make logs-db

# Acceder al shell de la BD
make db-shell

# Verificar variables de entorno
docker-compose exec web env | grep DATABASE
```

### Archivos estáticos no se cargan
```bash
# Recolectar archivos estáticos
make collectstatic

# Verificar permisos
docker-compose exec web ls -la /app/static
```

### Puerto ocupado
```bash
# Ver qué usa el puerto
sudo netstat -tulpn | grep :8000

# Cambiar puerto en docker-compose.yml
ports:
  - "8001:8000"
```

## 🔄 Migración a Producción

### 1. Configurar SSL
```bash
# Crear directorio para certificados
mkdir ssl

# Colocar certificados SSL
cp cert.pem ssl/
cp key.pem ssl/
```

### 2. Variables de Entorno
```bash
# Crear .env.prod
DEBUG=0
SECRET_KEY=tu-clave-secreta-segura
ALLOWED_HOSTS=tu-dominio.com
```

### 3. Levantar servicios
```bash
make prod-up
```

### 4. Verificar funcionamiento
```bash
make prod-logs
make status
```

## 📚 Recursos Adicionales

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- [Nginx Configuration](https://nginx.org/en/docs/)
- [PostgreSQL Docker](https://hub.docker.com/_/postgres)
- [Redis Docker](https://hub.docker.com/_/redis)

## 🤝 Contribución

Para contribuir a la configuración Docker:

1. Prueba los cambios localmente
2. Actualiza la documentación
3. Verifica que funcione en desarrollo y producción
4. Crea un pull request con descripción detallada

## 📞 Soporte

Si encuentras problemas:

1. Revisa los logs: `make logs`
2. Verifica el estado: `make status`
3. Consulta la documentación
4. Crea un issue con logs y pasos para reproducir
