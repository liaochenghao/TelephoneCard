import uuid

from django.db import transaction
from rest_framework import mixins, viewsets, serializers
from rest_framework.decorators import list_route
from rest_framework.response import Response
import logging
import re

from rest_framework.views import APIView

from activity_info.models import ActivityInfo
from activity_info.serializers import ActivityInfoSerializer
from record.models import ManMadeRecord
from user_info.models import UserInfo, UserDetailInfo, BackendUser
from user_info.serializers import UserInfoSerializer, UserDetailInfoSerializer
from utils.weixin_functions import WxInterfaceUtil
from utils.WXBizDataCrypt import WXBizDataCrypt
from utils.telephone_functions import TelephoneInterfaceUtil
from TelephoneCard.settings import WX_SMART_CONFIG

logger = logging.getLogger('django')


class UserInfoView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin,
                   mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    @list_route(['GET'])
    def authorize(self, request):
        """客户端登录获取授权"""
        code = request.query_params.get('code')
        if not code:
            raise serializers.ValidationError('Param code is none')
        res = WxInterfaceUtil.code_authorize(code)
        response = Response(res)
        return response

    @list_route(['POST'])
    @transaction.atomic
    def check_account(self, request):
        """
        检查用户信息
        :param request: 
        :return: 
        """
        params = request.data
        encryptedData = params.get('encryptedData')
        session_key = params.get('session_key')
        iv = params.get('iv')
        if not all((iv, encryptedData, session_key)):
            raise serializers.ValidationError('encryptedData、iv、session_key参数不能为空')
        user_info = UserInfo.objects.filter(openid=params.get('openid')).first()
        if not user_info:
            logger.info('系统错误：无法通过用户openid获取用户信息: openid=%s' % params.get('openid'))
            raise serializers.ValidationError('系统错误：无法通过用户openid获取用户信息: openid=%s' % params.get('openid'))
        update_user_tag = False
        if not user_info.unionid:
            update_user_tag = True
            # 如果用户未获取到unionid，则需要解密获取
            data = WXBizDataCrypt(WX_SMART_CONFIG['appid'], session_key)
            user_data = data.decrypt(encryptedData, iv)
            user_info.unionid = user_data.get('unionId')
        # 录入用户信息到数据库，同时也要注意微信用户可能会更换信息
        if user_info.nickname != params.get('nickname') or user_info.avatar_url != params.get('avatar_url'):
            update_user_tag = True
            user_info.nickname = params.get('nickname')
            user_info.gender = params.get('gender')
            user_info.province = params.get('province')
            user_info.country = params.get('country')
            user_info.city = params.get('city')
            user_info.avatar_url = params.get('avatar_url')
            user_info.language = params.get('language')
        if update_user_tag is True:
            user_info.save()
            logger.info('更新用户信息: openid=%s' % params.get('openid'))
        return Response()


class UserDetailInfoView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin,
                         mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = UserDetailInfo.objects.all()
    serializer_class = UserDetailInfoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        param = self.request.query_params
        openid = param.get('openid')
        status = param.get('status')
        if openid:
            queryset = queryset.filter(openid=openid)
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    @list_route(['GET'])
    def check_user_detail(self, request):
        """
        检查用户是否填写过基本信息
        :param request: 
        :return: true/false
        """
        params = request.query_params
        if not params.get('openid'):
            raise serializers.ValidationError('Param openid is none')
        user_detail_info = UserDetailInfo.objects.filter(user_id=params.get('openid')).first()
        return Response(True if user_detail_info else False)

    @list_route(['GET'])
    def message_code(self, request):
        params = request.query_params
        if not params.get('telephone'):
            raise serializers.ValidationError('Param telephone is none')
        phone_pat = re.compile("^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$")
        res = re.search(phone_pat, params.get('telephone'))
        if not res:
            raise serializers.ValidationError('Telephone is wrong')
        message_code = TelephoneInterfaceUtil.send_message(params.get('telephone'))
        return Response(message_code)

    @list_route(['GET'])
    def update_status(self, request):
        params = request.query_params
        openid = params.get('openid')
        status = params.get('status')
        if not all((openid, status)):
            raise serializers.ValidationError('Param (openid, status) is not none')
        if status not in ('0', '1', '2', '3'):
            raise serializers.ValidationError('Param status invalid')
        user_detail = UserDetailInfo.objects.filter(user_id=openid).first()
        if not user_detail:
            raise serializers.ValidationError('User Not Exist')
        user_detail.status = status
        user_detail.save()
        return Response()

    @list_route(['GET'])
    @transaction.atomic()
    def update_man_made_status(self, request):
        """
        人工审核修改状态
        :param request: 
        :return: 
        """
        params = request.query_params
        operator = params.get('operator')
        target_user_id = params.get('target_user_id')
        status = params.get('man_made_status')
        extra = params.get('extra')
        if not all((operator, target_user_id, status)):
            raise serializers.ValidationError('Param (operator, target_user_id, status) is not none')
        if status not in ('0', '1'):
            raise serializers.ValidationError('Param status invalid')
        user_detail = UserDetailInfo.objects.filter(user_id=target_user_id).first()
        if not user_detail:
            raise serializers.ValidationError('User Not Exist')
        if status == 0 and user_detail.status >= 2:
            raise serializers.ValidationError('快速通道已通过审核')
        user_detail.status = 1 if status == 0 else 2
        user_detail.man_made_status = status
        user_detail.save()
        # 将人工审核记录录入到后台数据库
        ManMadeRecord.objects.create(id=str(uuid.uuid4()), operator=operator, target_user=target_user_id, extra=extra)
        return Response()

    @list_route(['GET'])
    def get_user_status(self, request):
        params = request.query_params
        openid = params.get('openid')
        if not openid:
            raise serializers.ValidationError('param openid is none')
        user_detail = UserDetailInfo.objects.filter(user_id=openid).first()
        if not user_detail:
            raise serializers.ValidationError('User Not Exist')
        status = user_detail.status
        activity_info = ActivityInfo.objects.filter(type=status).first()
        result = dict()
        result['status'] = status
        result['activity_info'] = ActivityInfoSerializer(activity_info).data
        return Response(result)


class BackendUserView(APIView):
    def get(self, request):
        params = request.query_params
        username = params.get('username')
        password = params.get('password')
        user = BackendUser.objects.filter(user_name=username, password=password).first()
        return Response(True if user else False)
