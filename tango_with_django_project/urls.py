from django.contrib import admin
from django.conf.urls import url, include
from rango import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    # any url pattern starting with 'rango' is directed to the
    # rango urls.py file
    url(r'^rango/', include('rango.urls')),
]

