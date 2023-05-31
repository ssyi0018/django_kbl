import json
import random
from datetime import datetime
from django.shortcuts import render, HttpResponse
from scApp import models
from scApp.utils.bootstrap import BootStrapModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse




class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = '__all__'
        # 排除某个字段
        exclude = ['oid']


# 订单弹出框
def order_list(request):
    form = OrderModelForm()
    return render(request, 'order_list.html', {'form': form})


@csrf_exempt
def order_add(request):
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.instance.oid = datetime.now().strftime('%Y%m%d') + str(random.randint(1000, 9999))
        form.save()
        # 返回到Ajax里res
        # 下面两句意思相等
        return JsonResponse({'status': True})
        # return HttpResponse(json.dumps({'status': True}))

    data_dict = {'status': False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))
