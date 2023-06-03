from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


def chart_list(request):
    return render(request, 'chart_list.html')


def chart_bar(request):
    legend = ['张三', '李四']
    series_list = [
        {
            "name": '张三',
            "type": 'bar',
            "data": [5, 20, 36, 10, 10, 20, 99]
        },
        {
            "name": '李四',
            "type": 'bar',
            "data": [15, 30, 36, 10, 20, 40, 32]
        }
    ]
    date_list = ['一月', '二月', '三月', '四月', '五月', '六月', '七月']

    result = {
        'status': True,
        'data': {
            'legend': legend,
            'series_list': series_list,
            'date_list': date_list,
        }
    }
    # 把值传到前端
    return JsonResponse(result)


def chart_pie(request):
    db_data_list = [
        {'value': 2048, 'name': 'IT部门'},
        {'value': 1735, 'name': '运营部门'},
        {'value': 580, 'name': '测试部门'},
    ]

    result = {
        'status': True,
        'data': db_data_list,
    }
    # 把值传到前端
    return JsonResponse(result)


def chart_line(request):
    legend = ['上海', '深圳']
    series_list = [
        {
            'name': '上海',
            'type': 'line',
            'stack': 'Total',
            'data': [120, 132, 101, 134, 90, 230, 330]
        },
        {
            'name': '深圳',
            'type': 'line',
            'stack': 'Total',
            'data': [220, 182, 191, 234, 290, 330, 440]
        }
    ]
    x_axis = ['一月', '二月', '三月', '四月', '五月', '六月', '七月']

    result = {
        'status': True,
        'data': {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    # 把值传到前端
    return JsonResponse(result)
