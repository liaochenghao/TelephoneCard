from rest_framework import mixins, viewsets

from activity_info.models import ActivityInfo
from activity_info.serializers import ActivityInfoSerializer


class ActivityInfoView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin,
                       mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = ActivityInfo.objects.all()
    serializer_class = ActivityInfoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        param = self.request.query_params
        _id = param.get('id')
        _type = param.get('type')
        if _id:
            queryset = queryset.filter(id=_id)
        if _type:
            queryset = queryset.filter(type=_type)
        return queryset
