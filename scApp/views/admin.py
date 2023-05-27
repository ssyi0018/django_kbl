from django.shortcuts import render, redirect
from django import forms
from scApp import models
from scApp.utils.pagination import Pagination
from scApp.utils.bootstrap import BootStrapModelForm
from django.core.exceptions import ValidationError
from scApp.utils.encrypt import md5


class AdminForm(BootStrapModelForm):
    # 非数据库定义的字段
    confirm_password = forms.CharField(label='确认密码',
                                       widget=forms.PasswordInput(render_value=True),
                                       )

    class Meta:
        model = models.Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    # 钩子函数,针对fields里字段
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if confirm != pwd:
            raise ValidationError('密码不一致，请重新输入')
        # 返回到cleand_data里，再保存sava数据库
        return confirm


def admin_list(request):
    # 搜索
    # 通过url传参数搜索查询功能实现
    data_dict = {}
    search_data = request.GET.get('query', '')
    if search_data:
        data_dict['username__contains'] = search_data

    queryset = models.Admin.objects.filter(**data_dict)
    # 分页
    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        'search_data': search_data,
    }
    return render(request, 'admin_list.html', context)


def admin_add(request):
    title = '新建管理员'
    if request.method == 'GET':
        form = AdminForm()
        return render(request, 'add_public.html', {'form': form, 'title': title})
    # POST进行提交后校验
    form = AdminForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data) # 获取验证通过的所有数据，字典值
        form.save()
        return redirect("/admin/list/")
    else:
        return render(request, 'add_public.html', {'form': form, 'title': title})
