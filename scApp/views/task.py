import json
from django import forms
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from scApp.utils.bootstrap import BootStrapModelForm
from scApp import models
from scApp.utils.pagination import Pagination


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'
        widgets = {
            'detail': forms.Textarea
        }


def task_list(request):
    # 获取数据库所有任务
    queryset = models.Task.objects.all().order_by('-id')
    # 分页
    page_object = Pagination(request, queryset, page_size=2)
    form = TaskModelForm()
    # 对字段进行排序
    form.order_fields(['level', 'title', 'detail', 'user'])

    context = {'form': form,
               'queryset': page_object.page_queryset,
               'page_string': page_object.html(),
               }
    return render(request, 'task_list.html', context)


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
        # 返回到Ajax里res
        data_dict = {'status': True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {'status': False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))
