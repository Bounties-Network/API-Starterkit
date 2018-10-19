from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^auth/', include(('user.auth_urls'), namespace='auth')),
    url(r'^user/', include(('user.urls'), namespace='user')),
]
