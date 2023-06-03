from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    notes = models.CharField(verbose_name='备注', max_length=200, null=True, blank=True)
    # create_time = models.DateTimeField(verbose_name='创建时间')
    create_time = models.DateField(verbose_name='创建时间')

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


class PrettyNum(models.Model):
    mobile = models.CharField(verbose_name='手机号', max_length=11)
    price = models.IntegerField(verbose_name='价格', null=True, blank=True)

    level_choices = (
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)

    status_choices = (
        (1, '已占用'),
        (2, '未占用'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=2)


class Admin(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

    # 对象定制输出username字符串
    def __str__(self):
        return self.username


class Task(models.Model):
    level_choices = (
        (1, '紧急'),
        (2, '重要'),
        (3, '一般'),
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)
    title = models.CharField(verbose_name='标题', max_length=64)
    detail = models.TextField(verbose_name='详细信息')
    user = models.ForeignKey(verbose_name='负责人', to='Admin', on_delete=models.CASCADE)


class Order(models.Model):
    oid = models.CharField(verbose_name='订单号', max_length=64, blank=False)
    title = models.CharField(verbose_name='订单名称', max_length=32)
    price = models.IntegerField(verbose_name='订单价格')

    status_choices = (
        (1, '待支付'),
        (2, '已支付'),
    )
    status = models.SmallIntegerField(verbose_name='订单状态', choices=status_choices, default=1)
    admin = models.ForeignKey(verbose_name='管理员', to='Admin', on_delete=models.CASCADE)


class Boss(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=32)
    age = models.IntegerField(verbose_name='年龄')
    img = models.CharField(verbose_name='头像', max_length=128)


class City(models.Model):
    name = models.CharField(verbose_name='名称', max_length=32)
    count = models.IntegerField(verbose_name='人口')
    # 自动保存数据
    img = models.FileField(verbose_name='logo', max_length=128, upload_to='city/%Y-%m-%d')
