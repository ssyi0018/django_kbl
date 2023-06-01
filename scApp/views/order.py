import json
import random
from datetime import datetime
from django.shortcuts import render, HttpResponse
from scApp import models
from scApp.utils.bootstrap import BootStrapModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from scApp.utils.pagination import Pagination


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = '__all__'
        # 排除某个字段
        exclude = ['oid', 'admin']


# 订单弹出框
def order_list(request):
    queryset = models.Order.objects.all().order_by('-id')
    page_object = Pagination(request, queryset, page_size=5)
    form = OrderModelForm()
    context = {'form': form,
               'queryset': page_object.page_queryset,
               'page_string': page_object.html(),
               }
    return render(request, 'order_list.html', context)


@csrf_exempt
def order_add(request):
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.instance.oid = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000, 9999))
        # 获取account里登陆的session中id
        form.instance.admin_id = request.session['info']['id']
        form.save()
        # 返回到Ajax里res
        # 下面两句意思相等
        return JsonResponse({'status': True})
        # return HttpResponse(json.dumps({'status': True}))

    data_dict = {'status': False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))


def order_delete(request):
    uid = request.GET.get('uid')
    exists = models.Order.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({'status': False, 'error': '删除失败，数据不存在！'})
    models.Order.objects.filter(id=uid).delete()
    return JsonResponse({'status': True})


def order_detail(request):
    # 方式一
    uid = request.GET.get('uid')
    # 方式一
    # row_object = models.Order.objects.filter(id=uid).first()
    # 方式二，数据库获得字典
    row_dict = models.Order.objects.filter(id=uid).values('title','price','status').first()
    if not dict:
        return JsonResponse({'status': False, 'error': '数据不存在！'})
    # 获取数据库中对象row_object
    # result = {
    #     'status': True,
    #     'data': {
    #         'title': row_object.title,
    #         'price': row_object.price,
    #         'status': row_object.status,
    #     }
    # }
    result = {
        'status':True,
        'data':row_dict,
    }
    # 给前端res数据
    return JsonResponse(result)
