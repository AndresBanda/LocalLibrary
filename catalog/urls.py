# Use include() to add URLS from the catalog application 
from django.conf.urls import include, url
from . import views
urlpatterns = [
    #url(r'^catalog/', include('catalog.urls')),
    url(r'^$', views.index, name='index'),
]
