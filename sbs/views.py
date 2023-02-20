from django.shortcuts import render
from .models import TblSbsDms
from .serializers import SbsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


def test(request):
    s = SbsSerializer(instance=TblSbsDms.objects.using('sbs'), many=True)
    return Response(s.data, status=status.HTTP_200_OK)


def SbSData(request):
    if request.method == "GET":
        s = SbsSerializer(instance=TblSbsDms.objects.using('sbs'), many=True)
        return Response(data=s.data, status=status.HTTP_200_OK)



class SbsViewSet(ModelViewSet):
        queryset =  TblSbsDms.objects.using('sbs')
        serializer_class = SbsSerializer