
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',  views.home, name='home'),
    path('special-flavors/', include('special_flavors.urls'), name='special_flavors'),
    path('standard-flavors/', include('standard_flavors.urls'), name='standard_flavors'),
    path('admin/', admin.site.urls),
]