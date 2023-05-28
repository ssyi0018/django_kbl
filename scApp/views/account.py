from django.shortcuts import render, redirect, HttpResponse
from django import forms
from scApp.utils.bootstrap import BootStrapForm
from scApp.utils.encrypt import md5
from scApp import models


class LoginForm(BootStrapForm):
    # 字段名要和数据库表字段一致
    username = forms.CharField(label='用户名',
                               widget=forms.TextInput,
                               required=True, )
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(render_value=True),
                               required=True, )

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # 钩子方法里验证成功，获取用户名和密码
            # 直接在models里写
            # admin_object = models.Admin.objects.filter(username=form.cleaned_data['username'],
            #                                            password=form.cleaned_data['password'],).filter()
            # 通过字典获取，字段名要和数据库一致
            admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
            if not admin_object:
                # 错误信息
                form.add_error('password', '用户名或密码错误')
                return render(request, 'login.html', {'form': form})
            # 登录成功，cookie和session处理
            request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}
            return redirect('/admin/list')
        return render(request, 'login.html', {'form': form})
