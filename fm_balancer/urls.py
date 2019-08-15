"""fm_balancer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic.base import RedirectView
from django.urls import path,include
from django.conf import settings
from .views import logout_view,login_view,create_superuser

urlpatterns = [
    path(r'login/', login_view),
    path(r'logout/',logout_view),
    path(r'superuser/',create_superuser),
    path(r'dashboard/',include('dashboard.urls')),
    path(r'main/',include('main.urls')),
    path(r'proxy/',include('proxy.urls')),
    path(r'settings/',include('settings.urls')),
    path(r'',RedirectView.as_view(url='/dashboard/')),

]
