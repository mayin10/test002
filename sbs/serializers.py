
from rest_framework import serializers
from .models import TblSbsDms


class SbsSerializer(serializers.ModelSerializer):
        class Meta:
            model = TblSbsDms  # 写法和上面的CourseForm类似
            fields = '__all__'


