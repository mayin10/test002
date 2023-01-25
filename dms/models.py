from django.db import models
from django.contrib.auth.models import User
from db.base_model import BaseModel


class Role(BaseModel):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Employee(models.Model):
    company_choices = (
        (1, '01_company'),
        (2, '02_company'),
    )
    pos_choices = (
        (1, '01_intern'),
        (2, '02_extern'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=12)
    email_active = models.BooleanField(default=False)
    company = models.SmallIntegerField(default=1, choices=company_choices, verbose_name='Company')
    pos = models.SmallIntegerField(default=1, choices=pos_choices, verbose_name='Position')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
       return self.mobile


class Node(BaseModel):
    name = models.CharField(max_length=100)
    p_id = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    sort = models.IntegerField(default=50)

    def __str__(self):
       return self.node_name


class RoleNode(BaseModel):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)


class Site(BaseModel):
    name = models.CharField(max_length=100)
    desc = models.TextField(help_text="desc", verbose_name="desc")

    def __str__(self):
       return self.name


class Project(BaseModel):
    name = models.CharField(max_length=100)
    desc = models.TextField(help_text="desc", verbose_name="desc")
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
       return self.name


class Document(BaseModel):
    status_choices = (
        (1, 'in plan'),
        (2, 'in processing'),
        (3, 'Approved'),
    )
    documentID = models.CharField(max_length=100, unique=True)
    status = models.SmallIntegerField(default=1, choices=status_choices, verbose_name='status')
    version = models.IntegerField(default=0)
    desc = models.TextField(help_text="desc", verbose_name="desc")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = verbose_name
        ordering = ("documentID",)

    def __str__(self):
        return self.documentID

class Folder(BaseModel):
    name = models.CharField(max_length=200)
    p_id = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    sort = models.IntegerField(default=50)
    projectID = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class RoleFolder(BaseModel):
    right_choices = (
        (1, 'download'),
        (2, 'download + upload'),
        (3, 'download + upload + delete'),
    )

    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    right = models.SmallIntegerField(default=1, choices=right_choices, verbose_name='right')


class File(BaseModel):
    type_choices = (
        (1, 'doc'),
        (2, 'excel'),
        (3, 'pdf'),
        (4, 'image'),
        (5, 'dwg'),
    )
    name = models.CharField(max_length=200, default='')
    upload = models.FileField(upload_to='uploads/')
    size = models.CharField(max_length=100)
    version = models.IntegerField(default=0)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    type = models.SmallIntegerField(default=1, choices=type_choices, verbose_name='type')
    note = models.TextField(help_text="note", verbose_name="note")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

