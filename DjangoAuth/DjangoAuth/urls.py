from django.contrib import admin
from django.urls import path,include

from identity import urls as iurls
from frontend import urls as furls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include(iurls)),
    path('',include(furls)),
]
