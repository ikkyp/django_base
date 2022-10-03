from django.utils.deprecation import MiddlewareMixin


class TestMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print('请求前')
        username = request.COOKIES.get('name')
        if username is None:
            print('空的')
        else:
            print('有的')

    def process_response(self, request, response):
        print('请求后')
        return response
