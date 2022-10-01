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
