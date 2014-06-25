from django.conf.urls import patterns, url, include
from rest_framework import routers
from support import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.ProfileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^admin/', include(admin.site.urls)),
)
