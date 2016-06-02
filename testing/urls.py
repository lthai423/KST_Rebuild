from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'testing'

from . import views
urlpatterns = [

    url(r'^$', views.testing, name ='testing'),
    url(r'^launch/', views.launch, name ='launch'),
    url(r'^environment/', views.environment, name ='environment'),
    url(r'^ballistic/', views.ballistic, name ='ballistic'),
    url(r'^jet/', views.jet, name ='jet'),
    url(r'^protection/', views.protection, name ='protection'),
    url(r'^impact/', views.impact, name ='impact'),
    url(r'^seismic/', views.seismic, name ='seismic'),
    url(r'^fluids/', views.fluids, name ='fluids'),
    url(r'^electromagnetic/', views.electromagnetic, name ='electromagnetic'),
    url(r'^reliability/', views.reliability, name ='reliability'),
    url(r'^acoustics/', views.acoustics, name ='acoustics'),
    url(r'^technologies/', views.technologies, name = 'technologies'),
    url(r'^structural/', views.structural, name ='structural'),
    url(r'^engine/', views.engine, name ='engine'),
    url(r'^explosives/', views.explosives, name ='explosives'),
]

