"""mymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from operations import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^movies/', views.movies, name='movies'),
    url(r'^single/', views.single, name='single'),
    url(r'^tv_shows/', views.shows, name='tv_shows'),
    url(r'^history/', views.history, name='history'),
    url(r'^sports/', views.sports, name='sports'),
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('users.urls')),

]
