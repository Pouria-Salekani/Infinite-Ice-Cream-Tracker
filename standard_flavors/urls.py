from django.urls import path
from icecream import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.show_flavor, name='standard_flavors'),
]


# if settings.DEBUG is False:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)