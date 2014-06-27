import logging

from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from support import views
from django.contrib import admin
from kixeye import settings

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
admin.autodiscover()

urlpatterns = patterns('',
                       url('^users$',
                           views.profile_list,
                           name='profile-list'),
                       url('^users/(?P<pk>[0-9]+)$',
                           views.profile_detail,
                           name='profile-detail'),
                       url('^users/search',
                           views.profile_find,
                           name='profile-find'),
                       url('^battles',
                           views.battle_detail,
                           name='battle-detail'),
                       url(r'^api-auth/',
                           include('rest_framework.urls',
                                   namespace='rest_framework')),
                       url(r'^admin/',
                           include(admin.site.urls)),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
