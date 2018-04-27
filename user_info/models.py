from django.db import models


class UserInfo(models.Model):
    SEX_CHOICE = (
        (0, '未知'),
        (1, '男'),
        (2, '女')
    )
    openid = models.CharField('微信openid', max_length=60, primary_key=True)
    nickname = models.CharField('微信昵称', max_length=30, null=True)
    gender = models.IntegerField('性别', choices=SEX_CHOICE, default=0)
    avatar_url = models.CharField('微信头像url', max_length=255, null=True)
    city = models.CharField('城市', max_length=64, null=True)
    country = models.CharField('国家', max_length=64, null=True)
    province = models.CharField('省份', max_length=64, null=True)
    unionid = models.CharField('unionid', max_length=60, null=True, unique=True)
    session_key = models.CharField('微信用户标示', max_length=64)
    privilege = models.TextField('用户特权信息', null=True)
    language = models.CharField('语言', max_length=64, null=True)
    code = models.CharField('用户活动码', max_length=16, null=True)
    qr_code = models.CharField('用户邀请二维码', max_length=255, null=True)
    last_login = models.DateTimeField('最后登录时间', null=True)
    create_at = models.DateTimeField('创建时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'user_info'


class UserDetailInfo(models.Model):
    STATUS_CHOICE = (
        (0, '身份确认中'),
        (1, '身份验证失败'),
        (2, '待发卡'),
        (3, '已发卡'),
    )
    MAN_MADE_STATUS_CHOICE = (
        (-1, '人工审核暂未操作'),
        (0, '未通过人工认证身份'),
        (1, '通过人工认证身份')
    )
    USER_MADE_STATUS_CHOICE = (
        (-1, '初始状态'),
        (0, '未通过用户自己认证身份'),
        (1, '通过用户自己认证身份')
    )
    user = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, primary_key=True)
    c_name = models.CharField('中文名', max_length=30)
    country = models.CharField('国家', max_length=30)
    university = models.CharField('大学', max_length=60, null=True)
    email = models.CharField('邮箱', max_length=60, null=True)
    grade = models.CharField('年级', max_length=30, null=True)
    wechat = models.CharField('微信号', max_length=60, null=True)
    invite_code = models.CharField('邀请码', max_length=30, null=True)
    abroad_time = models.DateField('出国日期')
    recipients_name = models.CharField('收件人姓名', max_length=30)
    recipients_phone = models.CharField('收件人手机号', max_length=30)
    recipients_address = models.CharField('邮寄地址', max_length=60)
    recipients_number = models.CharField('快递单号', max_length=60, null=True)
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)
    man_made_status = models.IntegerField('人工审核状态', choices=MAN_MADE_STATUS_CHOICE, default=-1)
    user_made_status = models.IntegerField('用户审核状态', choices=USER_MADE_STATUS_CHOICE, default=-1)
    create_at = models.DateTimeField('创建时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'user_detail_info'


class BackendUser(models.Model):
    id = models.AutoField('序号', primary_key=True)
    user_name = models.CharField('用户名', max_length=64)
    password = models.CharField('密码', max_length=32)
    create_at = models.DateTimeField('创建时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'backend_user'
