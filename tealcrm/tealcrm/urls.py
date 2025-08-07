"""
URL configuration for tealcrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from core.views import index, about
from userprofile.views import signup

urlpatterns = [
    path('', index, name='index'),
    # url dashboard
    path('dashboard/', include('dashboard.urls')),
    # url lead
    path('dashboard/lead/', include('lead.urls')),
    # url client
    path('dashboard/client/', include('client.urls')),

    # authentication
    path('sign-up/', signup, name='signup'),
    path('log-in/', auth_views.LoginView.as_view(template_name='userprofile/log_in.html'), name='login'),
    path('log-out/', auth_views.LogoutView.as_view(), name='logout'),

    # pages section
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
]
