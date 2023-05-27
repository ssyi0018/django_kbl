from django.shortcuts import render, redirect
from scApp import models
from scApp.utils.pagination import Pagination
from scApp.utils.form import UserModelForm


def user_list(request):
    # for i in range(30):
    #     models.UserInfo.objects.create(name='test002', password='123456', age='22', account='12',
    #                                    create_time='2023-05-22',
    #                                    gender='2', depart_id='2', role_id='2', )

    # 通过url传参数搜索查询功能实现
    data_dict = {}
    search_data = request.GET.get('query', '')
    if search_data:
        data_dict['name__contains'] = search_data

    # 搜索条件
    queryset = models.UserInfo.objects.filter(**data_dict).order_by('id')

    # 调用分页封装函数,实例化对象
    page_object = Pagination(request, queryset, page_size=9)

    # 定义一个字典
    context = {'queryset01': page_object.page_queryset, 'search_data': search_data,
               'page_string': page_object.html()}
    # 当前页
    # try:
    #     page = int(request.GET.get('page', 1))  # 分页
    # except  ValueError:
    #     page = 1
    # page_size = 10  # 每页显示数据
    # start = (page - 1) * page_size
    # end = page * page_size

    # 数据总条数
    # total_num = models.UserInfo.objects.filter(**data_dict).order_by('id').count()
    #
    # # 计算出总页码 divmod函数计算商和余数
    # total_page, div = divmod(total_num, page_object.page_size)
    # if div:
    #     total_page += 1

    # # 根据当前页计算出前后5页
    # plus = 5
    # if total_page <= 2 * plus + 1:
    #     # 当数据库数据少的时候，没有达到11页
    #     start_page = 1
    #     end_page = total_page
    # else:
    #     # 数据库数据比较多，判断当前页,<5
    #     if page <= plus:
    #         start_page = 1
    #         end_page = 2 * plus
    #     else:
    #         # 当前页大于5
    #         if (page + plus) > total_page:
    #             start_page = total_page - 2 * plus
    #             end_page = total_page
    #         else:
    #             start_page = page - plus
    #             end_page = page + plus
    #
    # # 页码
    # page_list = []
    # page_list.append('<li><a href="?page={}">首页</a></li>'.format(1))
    # # 上一页
    # if page > 1:
    #     prev = '<li><a href="?page={}">上一页</a></li>'.format(page - 1)
    # else:
    #     prev = '<li><a href="?page={}">上一页</a></li>'.format(1)
    # page_list.append(prev)
    #
    # # 分页页面
    # for i in range(start_page, end_page + 1):
    #     if i == page:
    #         ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
    #     else:
    #         ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
    #     page_list.append(ele)
    #
    # # 下一页
    # if page < total_page:
    #     prev = '<li><a href="?page={}">下一页</a></li>'.format(page + 1)
    # else:
    #     prev = '<li><a href="?page={}">下一页</a></li>'.format(total_page)
    # page_list.append(prev)
    #
    # page_list.append('<li><a href="?page={}">尾页</a></li>'.format(total_page))
    #
    # search_tz = '''
    #              <li>
    #                 <form style="float: left;margin-left: -1px" method="get">
    #                     <input name="page"
    #                            style="position: relative;float: left;display: inline-block;width: 80px;border-radius: 0;"
    #                            type="text" class="form-control" placeholder="页码">
    #                     <button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
    #                     </span>
    #                 </form>
    #             </li>
    # '''
    # page_list.append(search_tz)
    #
    # # 导入mark_safe，把数据包裹成安全的传递给html
    # page_string = mark_safe(''.join(page_list))

    # queryset = models.UserInfo.objects.filter(name__contains=search_data)
    # print(queryset)

    # for obj in queryset:
    #     # obj.get_gender_display() 自动找定义的元组数据
    #     # obj.depart.title  # 获取关联表数据
    #     print(obj.create_time.strftime('%Y-%m-%d'), obj.get_gender_display(),
    #           obj.depart.title
    #           )
    # queryset = models.UserInfo.objects.filter(**data_dict).order_by('id')[page_object.start:page_object.end]

    return render(request, 'user_list.html', context)


def user_add(request):
    if request.method == 'GET':
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all(),
            'role_list': models.Role.objects.all(),
        }
        return render(request, 'user_add.html', context)

    # post获取页面value里数据
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    ac = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gd = request.POST.get('gd')
    dp = request.POST.get('dp')
    re = request.POST.get('re')

    models.UserInfo.objects.create(name=user, password=pwd, age=age, account=ac, create_time=ctime,
                                   gender=gd, depart_id=dp, role_id=re, )
    return redirect("/user/list/")


def user_modelform_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_modelform_add.html', {'form': form})

    # POST进行提交后校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect("/user/list/")
    else:
        return render(request, 'user_modelform_add.html', {'form': form})


def user_modelform_edit(request, nid):
    # 根据ID去数据库获取那一行数据（对象）
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method == 'GET':
        form1 = UserModelForm(instance=row_object)  # 实例化后获取默认值
        return render(request, 'user_modelform_edit.html', {'form': form1})  # 把数据传到html里
    # 更新这一行数据
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 如果不是界面需要输入的值保存，可以用
        # form.instance.字段名 = '某个值'
        form.save()
        return redirect("/user/list/")
    else:
        return render(request, 'user_modelform_add.html', {'form': form})


def user_modelform_del(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")
