from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'community'

from . import views
urlpatterns = [

    url(r'^/tech-employ/$', views.tech, name ='tech'),
    

]

