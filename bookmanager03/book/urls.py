from django.urls import path
from django.urls.converters import register_converter

from book.views import create_book, shop, register, jso, response, set_cookie, get_cookie, set_session
from book.views import get_session


# 定义转换器
class MobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return value

    # def to_url(self, value):
    #     return str(value)


# 注册转换器
register_converter(MobileConverter, 'phone')

urlpatterns = [
    path('create/', create_book),
    path('<int:city_id>/<phone:mobile>/', shop),
    path('register/', register),
    path('json/', jso),
    path('res/', response),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),
]
