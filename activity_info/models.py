from django.db import models


class ActivityInfo(models.Model):
    id = models.AutoField('编号', primary_key=True)
    text1 = models.TextField('说明一', max_length=255)
    text2 = models.TextField('说明二', max_length=255)
    text3 = models.TextField('说明三', max_length=255)
    text4 = models.TextField('说明四', max_length=255)
    text5 = models.TextField('说明五', max_length=255)
    create_at = models.DateTimeField('创建时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'activity_info'
