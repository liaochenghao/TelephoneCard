from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets, serializers
import logging
from record.models import InvitationRecord
from record.serializers import InvitationRecordSerializer

logger = logging.getLogger('django')


class InvitationRecordView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin,
                           mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = InvitationRecord.objects.all()
    serializer_class = InvitationRecordSerializer
