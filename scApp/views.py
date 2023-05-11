from django.shortcuts import render, HttpResponse, redirect
import requests


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


def news(request):
    # 爬虫取新闻
    url = "http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2023/05/news"
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(HTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    res = requests.get(url, headers=headers)

    # data_list = res.json()
    # print(data_list)

    try:
        #  判断响应码是否为200
        if res.status_code == 200:
            data_list = res.json()

            #  判断数据结构是否正确
            if isinstance(data_list, list):
                # print(data_list)
                return render(request, 'news.html', {'new_list': data_list})
            else:
                print("返回数据错误")
        else:
            print("请求失败", res.status_code)
    except Exception as e:
        print(e)

    # return render(request, 'news.html', {'new_list': data_list})


def something(request):
    print(request.method)

    print(request.GET)

    # return HttpResponse('返回内容')

    return render(request, 'something.html', {'title': 'come on'})

    # return redirect("http://www.baidu.com")


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # print(request.POST)
        username = request.POST.get("user")
        password = request.POST.get("pwd")

        if username == 'ssyi' and password == '000018':
            # return HttpResponse("登陆成功")
            return redirect("http://www.baidu.com")
        else:
            # return HttpResponse("用户名密码不正确!")
            return render(request, 'login.html', {'error_msg': '用户名或密码错误'})
