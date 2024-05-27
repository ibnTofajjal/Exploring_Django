
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    #Give Access to App all urls
    path('navigation/', include('navigation.urls'))
]
