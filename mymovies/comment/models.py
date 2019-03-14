from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now



MyUser = get_user_model()

# Create your models here.

class Comments(models.Model):
    content = models.CharField(max_length=255, verbose_name='评论的内容')
    user = models.ForeignKey(MyUser, verbose_name='评论用户')
    time = models.DateField(default=now, verbose_name='用户评论时间')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = '用户评论信息'
        verbose_name_plural = verbose_name