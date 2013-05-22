# -*- coding: utf-8 -*-

from django.conf.urls       import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic   import TemplateView
from django.conf            import settings

from noticias import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Index stacic page - Template view
    url(r'^$|^index/$', TemplateView.as_view(template_name='noticias/index.html'), name="noticias_index"),

    # List view
    url(r'^noticias/$', views.Noticias.as_view(), name="noticias"),

    # Create view
    url(r'^noticia/create/$', views.CreateNoticia.as_view(), name="create_noticia"),
    # Update view
    url(r'^noticia/update/(?P<pk>\d+)/$', views.UpdateNoticia.as_view(), name="update_noticia"),
    # Detail view
    url(r'^noticia/(?P<pk>\d+)/$', views.Noticia.as_view(), name="noticia"),
    # Delete view
    url(r'^noticia/delete/(?P<pk>\d+)/$', views.DeleteNoticia.as_view(), name="delete_noticia"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
