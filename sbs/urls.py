
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix="sbs", viewset=views.SbsViewSet)
urlpatterns = [
    path('SbSData', views.SbSData),
    path('test', views.test),
    path("", include(router.urls))
]
