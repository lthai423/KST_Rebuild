from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'testing'

from . import views
urlpatterns = [

    url(r'^environmental/$', views.environmental, name ='environmental'),
    url(r'^ballistic/$', views.ballistic, name ='ballistic'),
    url(r'^jet/$', views.jet, name ='jet'),
]

