from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    notes = models.CharField(verbose_name='备注', max_length=200, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间')
    # 级联删除
    # depart = models.ForeignKey(to='Department',to_fields='id',on_delete=models.CASCADE)
    # 置空
    role = models.ForeignKey(verbose_name='用户角色', to='Role', to_field='id', on_delete=models.CASCADE)
    depart = models.ForeignKey(verbose_name='用户部门', to='Department', to_field='id', null=True, blank=True,
                               on_delete=models.SET_NULL)
    gender_choices = (
        (1, '男'),
        (2, '女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)


class Department(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Role(models.Model):
    caption = models.CharField(max_length=16)

    def __str__(self):
        return self.caption
