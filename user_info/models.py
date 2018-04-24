from django.db import models


class UserInfo(models.Model):
    SEX_CHOICE = (
        (0, '未知'),
        (1, '男'),
        (2, '女')
    )
    openid = models.CharField('微信openid', max_length=60)
    nickname = models.CharField('微信昵称', max_length=30, null=True)
    sex = models.IntegerField('性别', choices=SEX_CHOICE, default=0)
    head_img_url = models.CharField('微信头像url', max_length=255, null=True)
    city = models.CharField('城市', max_length=64, null=True)
    country = models.CharField('国家', max_length=64, null=True)
    province = models.CharField('省份', max_length=64, null=True)
    unionid = models.CharField('unionid', max_length=60, null=True, unique=True)
    privilege = models.TextField('用户特权信息', null=True)
    create_at = models.DateTimeField('创建时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'user_info'


class DetailInfo(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
    c_name = models.CharField('中文名', max_length=30)
    country = models.CharField('国家', max_length=30)
    university = models.CharField('大学', max_length=60, null=True)
    email = models.CharField('邮箱', max_length=60, null=True)
    grade = models.CharField('年级', max_length=30, null=True)
    wechat = models.CharField('微信号', max_length=30, null=True)
    invite_code = models.CharField('邀请码', max_length=30, null=True)
    date = models.DateField('出国日期')
    name = models.CharField('收件人姓名', max_length=30)
    phone = models.CharField('收件人手机号', max_length=30)
    address = models.CharField('邮寄地址', max_length=30)

    class Meta:
        db_table = 'detail_info'
