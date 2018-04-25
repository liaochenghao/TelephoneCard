# coding: utf-8
from rest_framework import serializers

from record.models import InvitationRecord


class InvitationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationRecord
        fields = ['id', 'inviter', 'invitee', 'extra', 'create_at']
