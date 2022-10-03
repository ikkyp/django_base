import json

from django.shortcuts import HttpResponse

from book.models import BookInfo


# Create your views here.

def create_book(request):
    BookInfo.objects.create(
        name='abc',
        pub_date='2020-02-03',
        readcount=50,
    )
    return HttpResponse('create')


def shop(request, city_id, mobile):
    print(city_id, mobile)

    query_param = request.GET.getlist('p')
    print(query_param)
    return HttpResponse("成功啦")


def register(request):
    data = request.POST
    print(data)
    return HttpResponse("成功啦")


def jso(request):
    body = request.body.decode()
    print(type(body))
    # 将json格式的数据变化为字典格式
    body_dict = json.loads(body)
    print(body_dict)
    return HttpResponse("成功了")


def response(request):
    return HttpResponse("res")


def set_cookie(request):
    username = request.GET.get('username')
    res = HttpResponse("cookie")
    res.set_cookie('name', username, max_age=60 * 60)

    # 删除cookie
    res.delete_cookie('name')
    return res


def get_cookie(request):
    name = request.COOKIES.get('name')
    return HttpResponse(name)


def set_session(request):
    username = request.GET.get("username")
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username
    return HttpResponse("session")


def get_session(request):
    user_id = request.session.get('user_id')
    username = request.session.get('username')

    content = '{}, {}'.format(user_id, username)
    
    # 设置session过期时间
    request.session.set_expiry(3600)
    return HttpResponse(content)
