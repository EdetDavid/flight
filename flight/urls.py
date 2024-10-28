from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from demo import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Seplat OBT Superadmin"
admin.site.site_title = "Seplat OBT Superadmin Portal"
admin.site.index_title = "Seplat OBT Superadmin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.demo, name=''),
    path('', include('demo.urls')),

]


# Retrieve images from /media/
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
