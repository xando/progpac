from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from progpac.core import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^help/$', views.Help.as_view(), name='help'),
    url(r'^results/$', views.Results.as_view(), name='results'),
    url(r'^results/(?P<level_pk>\w+)/$', views.ResultsLevel.as_view(), name='results_level'),
    url(r'^level/(?P<level_hash>\w+)/$', views.Level.as_view(), name='level'),
    url(r'^credits/$', views.Credits.as_view(), name='credits'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

