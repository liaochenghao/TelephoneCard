# coding: utf-8
from rest_framework import serializers

from record.models import InvitationRecord, TelephoneChargesRecord


class InvitationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationRecord
        fields = ['id', 'inviter', 'invitee', 'invitee_nickname', 'invitee_avatar_url', 'extra', 'type', 'create_at']


class TelephoneChargesRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelephoneChargesRecord
        fields = ['id', 'user_id', 'operation', 'charge', 'balance', 'extra', 'create_at']
