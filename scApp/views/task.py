import json
from django import forms
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from scApp.utils.bootstrap import BootStrapModelForm
from scApp import models
from collections import OrderedDict
from django.forms.utils import ErrorDict


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'
        widgets = {
            'detail': forms.Textarea
        }


def task_list(request):
    form = TaskModelForm()
    # 对字段进行排序
    form.order_fields(['level', 'title', 'detail', 'user'])
    return render(request, 'task_list.html', {'form': form})


# @csrf_exempt免除post请求的csrf认证
@csrf_exempt
def task_ajax(request):
    print(request.GET)
    print(request.POST)

    data_dict = {'staus': True, 'data': [11, 2, 3, 3]}
    # json处理方式，转换成字符串
    # json_string = json.dumps(data_dict)
    return HttpResponse(json.dumps(data_dict))
    # django内部处理json格式
    # return JsonResponse(data_dict)


@csrf_exempt
def task_add(request):
    # print(request.POST)
    # 对数据校验
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {'status': True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {'status': False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))
