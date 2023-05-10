from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("欢迎ssyi")


def user_list(request):
    return render(request, 'user_list.html')


def user_add(request):
    return render(request, 'user_add.html')


def tpl(request):
    name = 'ssyi'
    roles = ['管理员', 'CEO', '保安']
    user_info = {'name': 'ssyi', 'salary': 100000, 'role': 'CTO'}

    data_list = [
        {'name': 'ssyi01', 'salary': 200000, 'role': 'COO'},
        {'name': 'ssyi02', 'salary': 400000, 'role': 'CAO'},
        {'name': 'ssyi03', 'salary': 500000, 'role': 'CWO'},
    ]

    return render(request, 'tpl.html', {'n1': name, 'n2': roles, 'n3': user_info, 'n4': data_list})
