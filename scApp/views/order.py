from django.shortcuts import render


# 订单弹出框
def order_list(request):
    return render(request, 'order_list.html')
