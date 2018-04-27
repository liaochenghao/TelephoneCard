# Create your views here.
import uuid

from rest_framework import mixins, viewsets, serializers
import logging
from django.db import transaction
from rest_framework.decorators import list_route
from rest_framework.response import Response

from record.models import InvitationRecord, TelephoneChargesRecord
from record.serializers import InvitationRecordSerializer, TelephoneChargesRecordSerializer
from user_info.models import UserInfo, UserDetailInfo
from record.utils import TelephoneChargesCompute

logger = logging.getLogger('django')


class InvitationRecordView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin,
                           mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = InvitationRecord.objects.all()
    serializer_class = InvitationRecordSerializer

    @transaction.atomic()
    @list_route(['GET'])
    def invitation(self, request):
        params = request.query_params
        invite_code = params.get('invite_code')
        unionid = params.get('unionid')
        if not all((invite_code, unionid)):
            raise serializers.ValidationError('Param (invite_code, unionid) must not be none')
        logger.info('=' * 70)
        logger.info('invite_code= %s ,unionid=%s' % (invite_code, unionid))
        logger.info('=' * 70)
        user_info = UserInfo.objects.filter(code=invite_code).first()
        if not user_info:
            raise serializers.ValidationError('邀请码无效，请仔细检查')
        InvitationRecord.objects.create(id=str(uuid.uuid4()), inviter=user_info.openid, invitee=unionid)
        total = InvitationRecord.objects.filter(inviter=user_info.openid).count()
        if total >= 3:
            # 快速通道审核成功
            user_detail_info = UserDetailInfo.objects.filter(user=user_info.openid).first()
            user_detail_info.user_made_status = 1
            user_detail_info.status = 3
            user_detail_info.save()
        return Response()


class TelephoneChargesRecordView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = TelephoneChargesRecord.objects.all()
    serializer_class = TelephoneChargesRecordSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        param = self.request.query_params
        user_id = param.get('user_id')
        operation = param.get('operation')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if operation:
            queryset = queryset.filter(operation=operation)
        return queryset

    @list_route(['GET'])
    @transaction.atomic()
    def get_telephone_charges(self, request):
        params = request.query_params
        code = params.get('code')
        user_id = params.get('user_id')
        if not all((code, user_id)):
            raise serializers.ValidationError('参数(code, user_id)不能为空')
        inviter = UserInfo.objects.filter(code=code).first()
        if not inviter:
            raise serializers.ValidationError('无法根据code获得邀请人')
        TelephoneChargesCompute.compute_telephone_charges(inviter.openid, 1, 10, extra='邀请用户' + user_id)
        TelephoneChargesCompute.compute_telephone_charges(user_id, 2, 10, extra='接受用户' + user_id + '邀请')
