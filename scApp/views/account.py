from django.shortcuts import render, redirect, HttpResponse
from django import forms
from scApp.utils.bootstrap import BootStrapForm
from scApp.utils.encrypt import md5
from scApp import models
from scApp.utils.code import check_code
from io import BytesIO


class LoginForm(BootStrapForm):
    # 字段名要和数据库表字段一致
    username = forms.CharField(label='用户名',
                               widget=forms.TextInput,
                               required=True, )
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(render_value=True),
                               required=True, )
    # 验证码字段自定义
    code = forms.CharField(label='验证码',
                           widget=forms.TextInput,
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
            # 验证码校验
            user_input_code = form.cleaned_data.pop('code')
            image_code = request.session.get('image_code', '')
            if image_code.upper() != user_input_code.upper():
                form.add_error('code', '验证码输入错误')
                return render(request, 'login.html', {'form': form})
            # print(form.cleaned_data)
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
            # 1天免登陆，session保存1天
            request.session.set_expiry(60 * 60 * 60)
            return redirect('/admin/list')
        return render(request, 'login.html', {'form': form})


def image_code(request):
    # 调用图片验证码
    img, code_string = check_code()

    # 写入到session，用于后面获取
    request.session['image_code'] = code_string
    # 设置session超时60秒
    request.session.set_expiry(60)
    # 创建一个内存文件
    stream = BytesIO()
    # 图片写入内存中
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def logout(request):
    request.session.clear()
    return redirect('/login/')
