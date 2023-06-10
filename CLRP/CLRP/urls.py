from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('Api.urls')),
    path('loyalty-app/',include('loyalty_app.urls')),


]
