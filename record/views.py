# Create your views here.
import uuid

from rest_framework import mixins, viewsets, serializers
import logging
from django.db import transaction
from rest_framework.decorators import list_route
from rest_framework.response import Response

from record.models import InvitationRecord
from record.serializers import InvitationRecordSerializer
from user_info.models import UserInfo, UserDetailInfo

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

