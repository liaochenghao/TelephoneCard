from django.db import transaction
from rest_framework import mixins, viewsets, serializers
from rest_framework.decorators import list_route
from rest_framework.response import Response
import logging
import re
from user_info.models import UserInfo, UserDetailInfo
from user_info.serializers import UserInfoSerializer, UserDetailInfoSerializer
from utils.weixin_functions import WxInterfaceUtil
from utils.telephone_functions import TelephoneInterfaceUtil
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
        iv = params.get('iv')
        if not (iv, encryptedData):
            raise serializers.ValidationError('encryptedData、iv参数不能为空')
        user_info = UserInfo.objects.filter(openid=params.get('openid')).first()
        if not user_info:
            logger.info('系统错误：无法通过用户openid获取用户信息: openid=%s' % params.get('openid'))
            raise serializers.ValidationError('系统错误：无法通过用户openid获取用户信息: openid=%s' % params.get('openid'))
        update_user_tag = False
        if not user_info.unionid:
            # 如果用户unionid不存在，则创建入库
            user_info.unionid = '123123123'
            update_user_tag = True
        # 录入用户信息到数据库，同时也要注意微信用户可能会更换信息
        if user_info.nick_name != params.get('nickname') or user_info.avatar_url != params.get('avatar_url'):
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
        user_detail_info = UserDetailInfo.objects.filter(openid=params.get('openid')).first()
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
