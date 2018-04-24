from rest_framework import mixins, viewsets

from activity_info.models import ActivityInfo
from activity_info.serializers import ActivityInfoSerializer


class ActivityInfoView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin,
                       mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = ActivityInfo.objects.all()
    serializer_class = ActivityInfoSerializer
