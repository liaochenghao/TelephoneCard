# coding: utf-8
from rest_framework import serializers
from user_info.models import UserInfo, UserDetailInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['openid', 'nickname', 'gender', 'avatar_url', 'city', 'country', 'province', 'unionid', 'session_key',
                  'privilege', 'language', 'code','qr_code', 'last_login', 'create_at']


class UserDetailInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetailInfo
        fields = ['user_id', 'c_name', 'country', 'university', 'email', 'grade', 'wechat', 'invite_code', 'abroad_time',
                  'recipients_name', 'recipients_phone', 'recipients_address', 'status', 'create_at']
        read_only_fields = ['user_id']

    def create(self, validated_data):
        data = self.context['request'].data
        validated_data['user_id'] = data.get('user_id')
        return super().create(validated_data)
