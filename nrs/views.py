from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from rest_framework.viewsets import ModelViewSet
from .models import DmsProjekte, DmsStatus, TblDmsProjectAdditionalData
from .serializers import DmsProjekteSerializer,DmsStatusSerializer,TblDmsProjectAdditionalDataSerializer



def test(request):
    list = []
    queryset= DmsStatus.objects.using('rpt')
    for e in queryset:
        list.append(e.project_status_id )
        list.append(e.datum_ist)
        print(e.datum_ist)
    return HttpResponse(list)


class DmsProjekteViewSet(ModelViewSet):
    queryset = DmsProjekte.objects.using('rpt')
    serializer_class = DmsProjekteSerializer

class DmsStatusViewSet(ModelViewSet):
    queryset = DmsStatus.objects.using('rpt')
    serializer_class = DmsStatusSerializer

class TblDmsProjectAdditionaViewSet(ModelViewSet):
    queryset = TblDmsProjectAdditionalData.objects.using('rpt')
    serializer_class = TblDmsProjectAdditionalDataSerializer