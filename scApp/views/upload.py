from django.shortcuts import render, HttpResponse
from django import forms
from scApp.utils.bootstrap import BootStrapForm, BootStrapModelForm
import os
from scApp import models
from django.conf import settings


class UpForm(BootStrapForm):
    # 移除某个字段样式
    bootstrap_exclude_fields = ['img']
    # 添加字段
    name = forms.CharField(label='姓名')
    age = forms.CharField(label='年龄')
    img = forms.FileField(label='头像')


def upload_list(request):
    if request.method == 'GET':
        return render(request, 'upload_list.html')
    # print(request.POST)
    # print(request.FILES)
    # 获取上传的文件对象
    file_object = request.FILES.get('avatar')
    # file_object.name 文件名字
    # 获取文件内容分块
    f = open(file_object.name, mode='wb')
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()

    return HttpResponse('..')


def upload_form(request):
    title = 'Form上传'
    if request.method == 'GET':
        form = UpForm()
        return render(request, 'upload_form.html', {'form': form, 'title': title})
    # 表单验证提交
    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 读取上传附件获取文件对象，写入到文件夹中，把附件路径存数据库
        img_object = form.cleaned_data.get("img")
        # 文件和数据库拼接
        # db_file_path = os.path.join("static", "img", img_object.name).replace('\\', '/')
        # file_path = os.path.join("scApp", db_file_path).replace('\\', '/')

        # 通过media拼接绝对路径
        # db_file_path = os.path.join(settings.MEDIA_ROOT, img_object.name).replace('\\', '/')
        # 相对路径
        db_file_path = os.path.join('scApp', 'media', img_object.name).replace('\\', '/')
        f = open(db_file_path, mode="wb")
        for chunk in img_object.chunks():
            f.write(chunk)
        f.close()
        # 写入数据库
        models.Boss.objects.create(
            name=form.cleaned_data['name'],
            age=form.cleaned_data['age'],
            img=db_file_path,
        )

        return HttpResponse('..')
    return render(request, 'upload_form.html', {'form': form, 'title': title})


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.City
        fields = '__all__'


def upload_modal_form(request):
    title = 'ModelForm上传'
    if request.method == 'GET':
        form = UpModelForm()
        return render(request, 'upload_form.html', {'form': form, 'title': title})
    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse('成功')
    return render(request, 'upload_form.html', {'form': form, 'title': title})
