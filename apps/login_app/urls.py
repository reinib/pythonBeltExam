from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create_user$', views.create_user),
    url(r'^login_user$', views.login_user),
    url(r'^logout_user$', views.logout),
]
