from django.conf.urls import include, url
from django.contrib import admin
from files.views import FileViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'files',FileViewSet)
urlpatterns = [
    # Examples:
    # url(r'^$', 'files_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
