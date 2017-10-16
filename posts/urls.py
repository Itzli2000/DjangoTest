from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^crear/$', views.post_create),
    url(r'^detalle/$', views.post_detail),
    url(r'^actualizar/$', views.post_update),
    url(r'^borrar/$', views.post_delete),
]
