from django.conf.urls import url
import django.contrib.auth.views
from . import views

urlpatterns = [
    url('gatapp', views.index, name='index'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'gatapp/login.html',
        },
        name='login'),
    url(r'^logout/$',
        django.contrib.auth.views.logout,
        {
            'template_name': 'gatapp/logout.html',
        },
        name='logout'),
    url(r'^temp/$', views.temp, name='temp'),
    url(r'^gitlab/$', views.private, name='gitlab')
]