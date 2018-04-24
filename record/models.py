from django.db import models


# Create your models here.
class InvitationRecord(models.Model):
    id = models.CharField('序列号', primary_key=True, max_length=64)
    inviter = models.CharField('邀请人编号', max_length=64)
    invitee = models.CharField('被邀请人编号', max_length=64)
    extra = models.CharField('备注信息', max_length=255, null=True)
    create_at = models.DateTimeField('邀请时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'invitation_record'
