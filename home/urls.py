from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

from . import views
urlpatterns = [
    url(r'^$', views.index, name ='index'),
]



#if settings.DEBUG is True:
#   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)