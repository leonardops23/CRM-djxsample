.PHONY: help build up down logs shell migrate collectstatic test clean

# Variables
COMPOSE_FILE = docker-compose.yml
COMPOSE_OVERRIDE = docker-compose.override.yml
COMPOSE_PROD = docker-compose.prod.yml

# Comandos principales
help: ## Mostrar esta ayuda
	@echo "Comandos disponibles:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

build: ## Construir las imágenes Docker
	docker-compose -f $(COMPOSE_FILE) build

up: ## Levantar los servicios en segundo plano
	docker-compose -f $(COMPOSE_FILE) up -d

down: ## Detener y eliminar los servicios
	docker-compose -f $(COMPOSE_FILE) down

logs: ## Mostrar logs de todos los servicios
	docker-compose -f $(COMPOSE_FILE) logs -f

logs-web: ## Mostrar logs del servicio web
	docker-compose -f $(COMPOSE_FILE) logs -f web

logs-db: ## Mostrar logs de la base de datos
	docker-compose -f $(COMPOSE_FILE) logs -f db

shell: ## Acceder al shell del contenedor web
	docker-compose -f $(COMPOSE_FILE) exec web bash

db-shell: ## Acceder al shell de PostgreSQL
	docker-compose -f $(COMPOSE_FILE) exec db psql -U crm_user -d crm_db

redis-cli: ## Acceder a Redis CLI
	docker-compose -f $(COMPOSE_FILE) exec redis redis-cli

migrate: ## Ejecutar migraciones
	docker-compose -f $(COMPOSE_FILE) exec web python manage.py migrate

makemigrations: ## Crear migraciones
	docker-compose -f $(COMPOSE_FILE) exec web python manage.py makemigrations

collectstatic: ## Recolectar archivos estáticos
	docker-compose -f $(COMPOSE_FILE) exec web python manage.py collectstatic --noinput

createsuperuser: ## Crear superusuario
	docker-compose -f $(COMPOSE_FILE) exec web python manage.py createsuperuser

test: ## Ejecutar tests
	docker-compose -f $(COMPOSE_FILE) exec web python manage.py test

# Comandos de desarrollo
dev-up: ## Levantar servicios para desarrollo
	docker-compose -f $(COMPOSE_FILE) -f $(COMPOSE_OVERRIDE) up -d

dev-down: ## Detener servicios de desarrollo
	docker-compose -f $(COMPOSE_FILE) -f $(COMPOSE_OVERRIDE) down

dev-shell: ## Shell para desarrollo
	docker-compose -f $(COMPOSE_FILE) -f $(COMPOSE_OVERRIDE) exec web bash

# Comandos de producción
prod-up: ## Levantar servicios de producción
	docker-compose -f $(COMPOSE_PROD) up -d

prod-down: ## Detener servicios de producción
	docker-compose -f $(COMPOSE_PROD) down

prod-logs: ## Logs de producción
	docker-compose -f $(COMPOSE_PROD) logs -f

# Comandos de limpieza
clean: ## Limpiar contenedores, imágenes y volúmenes no utilizados
	docker system prune -f
	docker volume prune -f

clean-all: ## Limpieza completa (¡CUIDADO!)
	docker system prune -a -f
	docker volume prune -f
	docker network prune -f

# Comandos de backup
backup: ## Crear backup de la base de datos
	docker-compose -f $(COMPOSE_FILE) run --rm backup

# Comandos de monitoreo
status: ## Mostrar estado de los servicios
	docker-compose -f $(COMPOSE_FILE) ps

top: ## Mostrar uso de recursos de los contenedores
	docker stats

# Comandos de red
network-ls: ## Listar redes Docker
	docker network ls

network-inspect: ## Inspeccionar red del proyecto
	docker network inspect crm-djxsample_crm_network

# Comandos de volúmenes
volume-ls: ## Listar volúmenes
	docker volume ls

volume-inspect: ## Inspeccionar volúmenes del proyecto
	docker volume inspect crm-djxsample_postgres_data crm-djxsample_static_volume crm-djxsample_media_volume
