from django.db import models


# Create your models here.
class InvitationRecord(models.Model):
    """
    邀请好友关注公众号记录表
    """
    id = models.CharField('序列号', primary_key=True, max_length=64)
    inviter = models.CharField('邀请人编号', max_length=64, db_index=True)
    invitee = models.CharField('被邀请人编号', max_length=64)
    invitee_nickname = models.CharField('被邀请人昵称', max_length=64)
    invitee_avatar_url = models.CharField('被邀请人头像', max_length=255)
    extra = models.CharField('备注信息', max_length=255, null=True)
    create_at = models.DateTimeField('邀请时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'invitation_record'
        ordering = ['-create_at']


class ManMadeRecord(models.Model):
    """
    人工审核记录表
    """
    id = models.CharField('序列号', primary_key=True, max_length=64)
    operator = models.CharField('操作人编号', max_length=64)
    target_user = models.CharField('被操作人编号', max_length=64)
    extra = models.CharField('备注信息', max_length=255, null=True)
    create_at = models.DateTimeField('邀请时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'man_made_record'
        ordering = ['-create_at']


class TelephoneChargesRecord(models.Model):
    """
    电话费用记录表
    """
    OPERATIONS_CHOICE = (
        (0, '初始话费'),
        (1, '邀请用户'),
        (2, '接受邀请'),

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
        ordering = ['-create_at']


class TelephoneCodeRecord(models.Model):
    id = models.CharField('序列号', primary_key=True, max_length=64)
    telephone = models.CharField('电话号码', max_length=64)
    code = models.CharField('短信验证码', max_length=64)
    create_at = models.DateTimeField('创建时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'telephone_code_record'
        ordering = ['-create_at']

