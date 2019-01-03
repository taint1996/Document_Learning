from django.conf.urls import url
from ce import views

urlpatterns = [
  url(r'^$', views.index),
]
