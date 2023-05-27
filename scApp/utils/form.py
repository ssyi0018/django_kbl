# 拆解form函数
from scApp import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from scApp.utils.bootstrap import BootStrapModelForm


# 继承自定义的modelform样式
class UserModelForm(BootStrapModelForm):
    # 输入长度验证规则
    name = forms.CharField(min_length=5,
                           label='姓名',
                           widget=forms.TextInput(attrs={'class': "form-control"}))
    # name = forms.CharField(disabled=True,label='姓名')  # 字段不可修改，或者直接在下面fields里去掉这个字段名即可
    # 正则表达式输入验证(方式一)
    age = forms.CharField(label='年龄啊',
                          validators=[RegexValidator(r'^[0-9]+$', '年龄请输入数字')]
                          )

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'depart', 'role']
        # fields = '__all__'  # 表示所有的字段
        # exclude = ['age']  # 排除某个字段

        # 插件里加样式
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': "form-control"}),
        #     'password': forms.PasswordInput(attrs={'class': "form-control"}),
        # }

    # 重写方法，循环找所有插件，进行重写class样式
    # def __init__(self, *args, **kwargs):
    #     super(UserModelForm, self).__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         # print(name, field)
    #         # 单独设置role角色不显示样式
    #         if name == 'role':
    #             continue
    #         field.widget.attrs = {'class': "form-control", 'placeholder': field.label}

    # 验证方式二(钩子方法)
    def clean_password(self):
        txt_pwd = self.cleaned_data['password']
        if len(txt_pwd) != 6:
            raise ValidationError("输入的位数错误")
        # 验证通过
        return txt_pwd

    # 判断姓名不允许重复(新建和编辑)
    def clean_name(self):
        # 排除当前编辑的一行ID exclude(self.instance.pk)

        txt_name = self.cleaned_data['name']
        exname = models.UserInfo.objects.exclude(id=self.instance.pk).filter(name=txt_name).exists()
        if exname:
            raise ValidationError('姓名不允许重复')
        return txt_name
