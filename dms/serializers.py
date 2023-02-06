from rest_framework import serializers
from .models import Employee,Role,Node, RoleNode,Document,Folder,File,RoleFolder,Site,Project
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


        def create(self, validated_data):
            user = get_user_model().objects.create_user(**validated_data)
            #user.is_staff = True
            # 密码加密
            #user.set_password(validated_data['password'])
            #user.save()
            return user

class EmployeeModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Employee
        fields = "__all__"


class RoleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ["id", "name"]

class NodeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Node
        fields = "__all__"

class RoleNodeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleNode
        fields = "__all__"


class SiteModelSerializer(serializers.ModelSerializer):
    #project = ProjectModelSerializer(many=True)
    class Meta:
        model = Site
        fields = ["id", "name"]






class DocumentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

class ProjectModelSerializer(serializers.ModelSerializer):
    site = SiteModelSerializer(many=False)

    class Meta:
        model = Project
        fields = "__all__"
class FolderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ["id","p_id", "name","projectID"]

class FileModelSerializer(serializers.ModelSerializer):

    document = DocumentModelSerializer(read_only=True, many=False)
    folder = FolderModelSerializer(read_only=True, many=False)
    class Meta:
        model =  File
        fields = "__all__"

class RoleFolderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleFolder
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

    def create(self, validated_data):
        uploadFile = super().create(validated_data)
        file = self.context['request'].FILES.get('upload')
        uploadFile.name = file.name
        uploadFile.size = file.size
        uploadFile.save()
        return uploadFile