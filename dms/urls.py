from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(prefix="employee", viewset=views.EmployeeViewSet)
router.register(prefix="user", viewset=views.UserViewSet)
router.register(prefix="role", viewset=views.RoleViewSet)
router.register(prefix="node", viewset=views.NodeViewSet)
router.register(prefix="role-node", viewset=views.RoleNodeViewSet)
router.register(prefix="site", viewset=views.SiteViewSet)
router.register(prefix="project", viewset=views.ProjectViewSet)
router.register(prefix="document", viewset=views.DocumentViewSet)
router.register(prefix="folder", viewset=views.FolderViewSet)
router.register(prefix="file", viewset=views.FileViewSet)
router.register(prefix="role-folder", viewset=views.RoleFolderViewSet)

urlpatterns = [
    path('test01', views.test01, name='test01'),
    path('test02', views.test02, name='test02'),
    path('testsite', views.testSite, name='testSite'),
    path('test', views.test, name='test'),
    path("", include(router.urls))
]