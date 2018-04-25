from django.db import models


class ActivityInfo(models.Model):
    TYPE_CHOICE = (
        (0, '活动信息'),
        (1, '信息审查'),
        (2, '信息审查失败信息'),
        (3, '等待福利快递发放'),
        (4, '福利已免费寄出'),
    )
    id = models.AutoField('编号', primary_key=True)
    text1 = models.TextField('说明一', max_length=255)
    text2 = models.TextField('说明二', max_length=255)
    text3 = models.TextField('说明三', max_length=255)
    text4 = models.TextField('说明四', max_length=255)
    text5 = models.TextField('说明五', max_length=255)
    type = models.IntegerField('类别')
    create_at = models.DateTimeField('创建时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'activity_info'
