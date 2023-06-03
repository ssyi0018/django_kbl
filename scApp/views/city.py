from django.shortcuts import render, HttpResponse, redirect
from scApp import models
from scApp.utils.bootstrap import BootStrapModelForm
from django import forms
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def city_list(request):
    queryset = models.City.objects.all()
    return render(request, 'city_list.html', {'queryset': queryset})


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.City
        fields = '__all__'


# def city_add(request):
#     title = '新建城市'
#     if request.method == 'GET':
#         form = UpModelForm()
#         return render(request, 'upload_form.html', {'form': form, 'title': title})
#     form = UpModelForm(data=request.POST, files=request.FILES)
#     if form.is_valid():
#         form.save()
#         return redirect('/city/list/')
#     return render(request, 'upload_form.html', {'form': form, 'title': title})

def city_add(request):
    title = '新建城市'
    if request.method == 'GET':
        form = UpModelForm()
        return render(request, 'upload_form.html', {'form': form, 'title': title})
    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        file_ext = request.FILES['img'].name.split('.')[-1]
        if file_ext == 'xls' or file_ext == 'xlsx':
            # fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            # filename = fs.save(request.FILES['img'].name, request.FILES['img'])
            # uploaded_file_url = fs.url(filename)
            form.instance.img.name = request.FILES['img'].name
        form.save()
        return redirect('/city/list/')
    return render(request, 'upload_form.html', {'form': form, 'title': title})
