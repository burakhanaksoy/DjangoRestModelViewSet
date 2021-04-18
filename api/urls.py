from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('carspecs', views.CarSpecsViewSet,basename='carspecs')

urlpatterns = [
    url('', include(router.urls))
]
