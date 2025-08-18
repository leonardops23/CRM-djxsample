# 🏢 CRM System - Sistema de Gestión de Relaciones con Clientes

[![Django](https://img.shields.io/badge/Django-5.2.5-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Descripción

CRM System es una aplicación web completa desarrollada en Django para la gestión integral de relaciones con clientes. Permite administrar clientes, oportunidades de venta, tareas y contactos de manera eficiente y organizada.

## ✨ Características Principales

### 🎯 **Gestión de Clientes**
- Registro completo de información de clientes
- Historial de interacciones y contactos
- Seguimiento de oportunidades asociadas
- Gestión de tareas relacionadas

### 🏆 **Gestión de Oportunidades**
- Creación y seguimiento de oportunidades de venta
- Estados personalizables (Nueva, En Progreso, Ganada, Perdida)
- Valoración económica y probabilidad de cierre
- Fechas de cierre y seguimiento

### ✅ **Sistema de Tareas**
- Creación y asignación de tareas
- Prioridades configurables (Alta, Media, Baja)
- Estados de progreso (Pendiente, En Progreso, Completada)
- Fechas de vencimiento y recordatorios

### 📞 **Gestión de Contactos**
- Registro de todas las interacciones con clientes
- Tipos de contacto configurables
- Seguimiento de resultados y próximas acciones
- Historial completo de comunicación

### 📊 **Dashboard Inteligente**
- Estadísticas en tiempo real
- Gráficos de oportunidades por estado
- Tareas próximas a vencer
- Métricas de rendimiento

## 🖼️ Capturas de Pantalla

### Dashboard Principal
![Dashboard](docs/images/dashboard.png)
*Vista general del sistema con estadísticas y métricas clave*

### Lista de Clientes
![Clientes](docs/images/clientes.png)
*Gestión completa de clientes con búsqueda y filtros*

### Formulario de Oportunidades
![Oportunidades](docs/images/oportunidades.png)
*Creación y edición de oportunidades de venta*

### Sistema de Tareas
![Tareas](docs/images/tareas.png)
*Gestión de tareas con prioridades y estados*

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/CRM-djxsample.git
cd CRM-djxsample
```

2. **Crear entorno virtual**
```bash
python -m venv env
source env/bin/activate  # En Linux/Mac
# o
env\Scripts\activate     # En Windows
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar base de datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario**
```bash
python manage.py createsuperuser
```

6. **Ejecutar el servidor**
```bash
python manage.py runserver
```

### Acceso al Sistema
- **URL**: http://127.0.0.1:8000/
- **Usuario por defecto**: admin
- **Contraseña por defecto**: admin

## 🛠️ Tecnologías Utilizadas

### Backend
- **Django 5.2.5** - Framework web de alto nivel
- **SQLite** - Base de datos ligera (configurable para producción)
- **Python 3.8+** - Lenguaje de programación

### Frontend
- **Bootstrap 5.3.0** - Framework CSS responsive
- **Bootstrap Icons** - Iconografía moderna
- **JavaScript ES6+** - Interactividad del lado del cliente

### Herramientas Adicionales
- **Django Crispy Forms** - Formularios con mejor presentación
- **Crispy Bootstrap5** - Integración con Bootstrap 5

## 📁 Estructura del Proyecto

```
CRM-djxsample/
├── core/                           # Aplicación principal
│   ├── models.py                  # Modelos de datos
│   ├── views.py                   # Vistas y lógica de negocio
│   ├── forms.py                   # Formularios
│   ├── admin.py                   # Configuración del admin
│   └── urls.py                    # URLs de la aplicación
├── res_crm/                       # Configuración del proyecto
│   ├── settings.py                # Configuración general
│   ├── urls.py                    # URLs principales
│   └── wsgi.py                    # Configuración WSGI
├── templates/                      # Plantillas HTML
│   ├── base.html                  # Plantilla base
│   └── crm/                       # Plantillas específicas
│       ├── dashboard.html         # Dashboard principal
│       ├── cliente_*.html         # Plantillas de clientes
│       ├── oportunidad_*.html     # Plantillas de oportunidades
│       └── tarea_*.html           # Plantillas de tareas
├── static/                        # Archivos estáticos
├── requirements.txt               # Dependencias del proyecto
└── manage.py                     # Script de gestión de Django
```

## 🔧 Configuración

### Variables de Entorno
Crea un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Configuración de Base de Datos
El proyecto está configurado para usar SQLite por defecto. Para producción, puedes cambiar a PostgreSQL o MySQL en `res_crm/settings.py`.

## 📱 Características Responsive

- **Mobile First**: Diseño optimizado para dispositivos móviles
- **Responsive**: Se adapta a todos los tamaños de pantalla
- **Touch Friendly**: Interfaz optimizada para pantallas táctiles

## 🔐 Seguridad

- **Autenticación**: Sistema de login/logout integrado
- **Autorización**: Control de acceso basado en usuarios
- **CSRF Protection**: Protección contra ataques CSRF
- **XSS Protection**: Protección contra ataques XSS

## 🧪 Testing

```bash
# Ejecutar tests
python manage.py test

# Ejecutar tests con cobertura
coverage run --source='.' manage.py test
coverage report
```

## 📦 Despliegue

### Docker (Recomendado)
```bash
# Construir imagen
docker build -t crm-system .

# Ejecutar contenedor
docker run -p 8000:8000 crm-system
```

### Despliegue Manual
1. Configurar servidor web (Nginx/Apache)
2. Configurar WSGI (Gunicorn/uWSGI)
3. Configurar base de datos de producción
4. Configurar variables de entorno
5. Ejecutar migraciones

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- **Tu Nombre** - *Desarrollo inicial* - [TuUsuario](https://github.com/TuUsuario)

## 🙏 Agradecimientos

- Django Software Foundation por el excelente framework
- Bootstrap Team por el framework CSS
- Comunidad de desarrolladores Python/Django

## 📞 Soporte

Si tienes alguna pregunta o necesitas ayuda:

- 📧 Email: tu-email@ejemplo.com
- 🐛 Issues: [GitHub Issues](https://github.com/tu-usuario/CRM-djxsample/issues)
- 📖 Documentación: [Wiki del Proyecto](https://github.com/tu-usuario/CRM-djxsample/wiki)

## 🔄 Historial de Versiones

- **v1.0.0** - Versión inicial con funcionalidades básicas
- **v1.1.0** - Agregado sistema de tareas
- **v1.2.0** - Mejoras en el dashboard y reportes

---

⭐ **¡No olvides dar una estrella al proyecto si te ha sido útil!**
