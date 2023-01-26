"""dms01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    ##media配置——配合settings中的MEDIA_ROOT的配置，就可以在浏览器的地址栏访问media文件夹及里面的文件了
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}, name='static'),
    path("api-token-auth/", views.obtain_auth_token),  # Token post
    path("api-auth/", include("rest_framework.urls")),
    path("docs/", include_docs_urls(title="NRS DMS API", description="NRS DMS Django REST framework")),
    path('admin/', admin.site.urls),
    path("dmsAPi/", include("dms.urls")),
    path("nrs/", include("nrs.urls")),
]
