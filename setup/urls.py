from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from eletro.views import EletroViewSet

router = routers.DefaultRouter()
router.register('eletro',EletroViewSet )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
