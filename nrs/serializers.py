from rest_framework import serializers
from .models import DmsProjekte, DmsStatus, TblDmsProjectAdditionalData


class DmsProjekteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DmsProjekte
        fields = "__all__"

class DmsStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DmsStatus
        fields = "__all__"

class TblDmsProjectAdditionalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblDmsProjectAdditionalData
        fields = "__all__"
