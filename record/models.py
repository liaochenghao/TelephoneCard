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


class ManMadeRecord(models.Model):
    id = models.CharField('序列号', primary_key=True, max_length=64)
    operator = models.CharField('操作人编号', max_length=64)
    target_user = models.CharField('被操作人编号', max_length=64)
    extra = models.CharField('备注信息', max_length=255, null=True)
    create_at = models.DateTimeField('邀请时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'man_made_record'


class TelephoneChargesRecord(models.Model):
    OPERATIONS_CHOICE = (
        (0, '初始话费'),
        (1, '邀请用户'),
    )
    id = models.CharField('序列号', primary_key=True, max_length=64)
    user_id = models.CharField('用户编号', max_length=64)
    operation = models.IntegerField(choices=OPERATIONS_CHOICE)
    charge = models.IntegerField('费用金额')
    balance = models.IntegerField('余额')
    extra = models.CharField('备注信息', max_length=255, null=True)
    create_at = models.DateTimeField('创建时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'telephone_charges_record'
