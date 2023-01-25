from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(prefix="project", viewset=views.DmsProjekteViewSet)


urlpatterns = [
    path('test', views.test, name='test'),
    path("", include(router.urls))
]