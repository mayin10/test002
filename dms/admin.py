from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Employee,Role,Node, RoleNode,Document,Folder,File,RoleFolder,Site,Project


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', 'create_time','create_by')
    search_fields = fields
    list_filter = fields

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    fields = ['name','p_id','level']
    list_display = ('name','p_id','level', 'create_time','create_by')

@admin.register(RoleNode)
class RoleNodeAdmin(admin.ModelAdmin):
    list_display = ('role_id', 'node_id' ,'create_time', 'create_by')

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "desc")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "desc")

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "documentID", "status", "version")

@admin.register(Folder)
class Folder(admin.ModelAdmin):
    list_display = ("id","name", "level")

@admin.register(RoleFolder)
class RoleNodeAdmin(admin.ModelAdmin):
    list_display = ("id","role_id")


@admin.register(File)
class File(admin.ModelAdmin):
    list_display = ("id","name")


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)