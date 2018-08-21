from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_job$', views.add_job),
    url(r'^create_job$', views.create_job),
    url(r'^createJoin/(?P<job_id>\d+)$', views.createJoin),
    url(r'^destroyJoin/(?P<job_id>\d+)$', views.destroyJoin),
    url(r'^show/(?P<job_id>\d+)$', views.show),
    url(r'^edit/(?P<job_id>\d+)$', views.edit),
    url(r'^update/(?P<job_id>\d+)$', views.update),
    url(r'^delete/(?P<job_id>\d+)$', views.delete),
]
