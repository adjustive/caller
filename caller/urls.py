"""caller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from dj]ango.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

#from dialer.views import SupportTicketCreate

urlpatterns = [
    url(r'^dialer/', include('dialer.urls')),
    
    #url(r'^$', SupportTicketCreate.as_view(), name='home'),
    #url(r'^support/', include('browser_calls.urls')),
    
    url(r'^admin/', admin.site.urls),
]
