"""
Definition of urls for LocalLibrary.
"""

from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
'''
urlpatterns =[
    # Examples:
    # url(r'^$', LocalLibrary.views.home, name='home'),
    # url(r'^LocalLibrary/', include('LocalLibrary.LocalLibrary.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]'''
urlpatterns = [
    url(r'^admin/', admin.site.urls), 
    url(r'^catalog/', include('catalog.urls')),
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)