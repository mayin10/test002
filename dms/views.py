from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.viewsets import ModelViewSet
from .models import Employee,Role,Node, RoleNode,Document,Folder,File,RoleFolder,Site,Project
from .serializers import EmployeeModelSerializer,RoleModelSerializer,NodeModelSerializer,RoleNodeModelSerializer,UserModelSerializer
from .serializers import DocumentModelSerializer,FolderModelSerializer,FileModelSerializer,RoleFolderModelSerializer,FileSerializer
from .serializers import SiteModelSerializer,ProjectModelSerializer
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
import os
from django.core import serializers
import json


def test01(request):
    folder = Folder.objects.all()
    output = ', '.join([q.name for q in folder])
    return render(request, 'dms/test.html',{'folder':folder})
    #return HttpResponse(output)

def test02(request):
    folder = Folder.objects.all()
    output = ', '.join([q.name for q in folder])
    return render(request, 'dms/testSite.html',{'folder':folder})
    #return HttpResponse(output)


def testSite(request):
    data = Site.objects.all()
    list = []
    for d1 in data:
        tinydict = {'id': d1.id, 'text': d1.name, 'expanded':True}
        list.append(tinydict)
    return render(request, 'dms/testSite.html', {'output': list})








# token wird auto erzeugt
@receiver(post_save, sender=settings.AUTH_USER_MODEL)  # Django的信号机制
def generate_token(sender, instance=None, created=False, **kwargs):
    """
    创建用户时自动生成Token
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        Token.objects.create(user=instance)


def test(request):
    base = os.path.abspath('.') + "\\static\\DOKUMENTE\\123990708\\123990708"

    '''
        list = []
    list2=[]
    for dirpath, dirnames, filenames in os.walk(base):
        s = dirpath.split("\\")
        if len(s) > 9:
            print(s[9])
    
                foderid = Folder.objects.get(name=s[7]).id
            folder = Folder(name=s[8],p_id = foderid, level = 2)
            folder.save()
        for l in list2[0]:
        print(l)
        folder = Folder(name=l, p_id=0, level=1)
        folder.save()
        base = os.path.abspath('.') + "\\static\\DOKUMENTE\\123990708"
    list =[]
    for dirpath, dirnames, filenames in os.walk(base):
         s = dirpath.split("\\")
         if len(s) == 8:
             pid = Folder.objects.get(folder_name=s[6]).id
             folder = Folder(folder_name=s[7],p_id = pid, level = 1)
             folder.save()


        base = os.path.abspath('.') + "\\static\\DOKUMENTE\\123990708"
    for dirpath, dirnames, filenames in os.walk(base):
        # list = dirpath.split("\\")
        for filename in filenames:
            s = os.path.join(dirpath, filename).split("\\")
            if len(s) > 7:
                foderid = Folder.objects.get(folder_name=s[len(s) - 2]).id
                file = File(file_name=s[len(s)-1], version=1, document_id=1, folder_id=foderid)
                file.save()
    '''
    print(base)
    return HttpResponse(base)



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword == '':
            return User.objects.all()
        elif keyword is None:
            return User.objects.all()
        else:
            return User.objects.filter(username__contains=keyword)|User.objects.filter(email__contains=keyword)


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    #queryset = Role.objects.using('nrs_dms')
    serializer_class = RoleModelSerializer

class NodeViewSet(ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = RoleNodeModelSerializer

class RoleNodeViewSet(ModelViewSet):
    queryset = RoleNode.objects.all()
    serializer_class = NodeModelSerializer


class SiteViewSet(ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteModelSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentModelSerializer


class FolderViewSet(ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderModelSerializer

class FileViewSet(ModelViewSet):
   # queryset = File.objects.all()
   queryset = File.objects.order_by("-id")
   serializer_class = FileModelSerializer


class RoleFolderViewSet(ModelViewSet):
    queryset = RoleFolder.objects.all()
    serializer_class = RoleFolderModelSerializer
#http://127.0.0.1:8000/dmsAPi/role-folder/?page=1&pagesize=100&role_id=3
    def get_queryset(self):
        role_id = self.request.query_params.get('role_id')
        if role_id == '':
            return RoleFolder.objects.all()
        elif role_id is None:
            return RoleFolder.objects.all()
        else:
            return RoleFolder.objects.filter(role_id=role_id)





class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer