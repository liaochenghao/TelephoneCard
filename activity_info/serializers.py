# coding: utf-8
from rest_framework import serializers
from activity_info.models import ActivityInfo


class ActivityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityInfo
        fields = ['id', 'text1', 'text2', 'text3', 'text4', 'text5', 'create_at']

