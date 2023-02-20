from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.viewsets import ModelViewSet
from .models import Employee,Role,Node, RoleNode,Document,Folder,File,RoleFolder,Site,Project,FileCount
from .serializers import EmployeeModelSerializer,RoleModelSerializer,NodeModelSerializer,RoleNodeModelSerializer,UserModelSerializer
from .serializers import DocumentModelSerializer,FolderModelSerializer,RoleFolderModelSerializer,FileSerializer
from .serializers import SiteModelSerializer,ProjectModelSerializer,FileCountSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import os
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import tempfile
import zipfile
from django.conf import settings
import datetime



def test01(request):

    forder_id = 16

    temp = tempfile.TemporaryFile()
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
    file = File.objects.filter(folder_id = forder_id)

    for f in file:
        file_path= os.path.join(settings.MEDIA_ROOT, f.upload.path)
        file_name = getFileName(forder_id,f.name)
        archive.write(file_path, file_name)
    archive.close()
    lenth = temp.tell()
    temp.seek(0)
    wrapper = FileWrapper(temp)
    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=archive.zip'
    response['Content-Length'] = lenth  # temp.tell()
    return response


def test02(request):
    id = 16
    f = Folder.objects.get(pk=id)
    ids = []
    if f.p_id == 0:
      folders = Folder.objects.filter(p_id=id)
      for cf in folders:
            ids.append(cf.id)

      if len(ids) > 0:
         files = File.objects.filter(folder_id__in=ids)


    return  HttpResponse('ok')


def zipDownload(request, folder_id,projekt_id):
    projekt_id = projekt_id
    folder_id = folder_id
    file = []
    if folder_id == 0:
        file = File.objects.filter(projekt_id=projekt_id)
    else:
        f = Folder.objects.get(pk=folder_id)
        ids = []
        if f.p_id == 0:
          folders = Folder.objects.filter(p_id=folder_id)
          for cf in folders:
                ids.append(cf.id)

          if len(ids) > 0:
            file = File.objects.filter(folder_id__in=ids).filter(projekt_id=projekt_id)
          else:
            file = File.objects.filter(folder_id=folder_id).filter(projekt_id=projekt_id)

    temp = tempfile.TemporaryFile()
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
    for f in file:
        file_path = os.path.join(settings.MEDIA_ROOT, f.upload.path)
        file_name = getFileName(f.folder_id, f.name,projekt_id)
        archive.write(file_path, file_name)
    archive.close()
    lenth = temp.tell()
    temp.seek(0)
    wrapper = FileWrapper(temp)
    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=zipDownload.zip'
    response['Content-Length'] = lenth  # temp.tell()
    return response


def getFileName(id, file_name,projekt_id):
    name = ''
    f = Folder.objects.get(pk=id)
    name = os.path.join(f.name, file_name)
    if f.p_id > 0:
        pf = Folder.objects.get(pk=f.p_id)
        name1 = os.path.join(pf.name, name)
       #name = os.path.join(str(projekt_id), name1)
    return name1






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

    def get_queryset(self):
        doku_container_id = self.request.query_params.get('doku_container_id')
        if doku_container_id == '':
            return  Folder.objects.all()
        elif doku_container_id is None:
            return Folder.objects.all()
        else:
            return Folder.objects.filter(doku_container_id = doku_container_id)



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
    def get_queryset(self):
        projekt_id = self.request.query_params.get('projekt_id')
        if projekt_id == '':
            return  File.objects.all()
        elif projekt_id is None:
            return File.objects.all()
        else:
            return File.objects.filter(projekt_id = projekt_id)

class FileCountViewSet(ModelViewSet):

    queryset = FileCount.objects.all()
    serializer_class = FileCountSerializer
    def get_queryset(self):
        projekt_id = self.request.query_params.get('projekt_id')
        if projekt_id == '':
            return  FileCount.objects.all()
        elif projekt_id is None:
            return FileCount.objects.all()
        else:
            return FileCount.objects.filter(projekt_id = projekt_id)