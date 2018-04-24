from rest_framework import mixins, viewsets

from user_info.models import UserInfo, UserDetailInfo
from user_info.serializers import UserInfoSerializer, UserDetailInfoSerializer


class UserInfoView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin,
                   mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class UserDetailInfoView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin,
                         mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = UserDetailInfo.objects.all()
    serializer_class = UserDetailInfoSerializer
