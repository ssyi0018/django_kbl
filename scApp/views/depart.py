from django.shortcuts import render, HttpResponse, redirect
from scApp import models


def depart_list(request):
    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html', {'queryset': queryset})


def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    # 获取post提交内容
    name = request.POST.get('title')
    # 保存数据
    models.Department.objects.create(title=name)
    # 重定向到列表页面
    return redirect("/depart/list/")


def depart_del(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    # return HttpResponse('删除成功')
    return redirect("/depart/list/")


def depart_edit(request, nid):
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        # 重定向到列表页面
        return render(request, 'depart_edit.html', {'row_object': row_object})

    # 获取post提交内容
    name = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=name)
    return redirect("/depart/list/")
