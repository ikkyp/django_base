from django.shortcuts import render

from book.models import BookInfo, PeopleInfo


# Create your views here.
def index(request):
    context = {
        'name': 'hahaha876tr',
    }

    # 增加数据
    '''
    BookInfo.objects.create(
        name='增加数据',
        pub_date='2022-10-01',
        readcount=40,
        commentcount=50,
        is_delete=0,
    )
    '''

    # 更新数据
    # BookInfo.objects.filter(id=1).update(readcount=70)

    # 删除数据
    # BookInfo.objects.get(id=5).delete()

    # 查询数据(get查询的是一个数据，filter查询出来的是一个列表，可以有多个数据，all是所有数据， count是计算数量加不加all都一样)
    '''
    BookInfo.objects.get(pk=1)
    BookInfo.objects.filter(pk=1)
    BookInfo.objects.all().count()
    BookInfo.objects.count()
    '''

    # 用F函数比较两个字段的值
    # from django.db.models import F
    # BookInfo.objects.filter(readcount__gte=F('commentcount'))

    # 用Q函数判断多个条件符合一个的对象
    # from django.db.models import Q
    # BookInfo.objects.filter(Q(readcount__gt=10) | Q(commentcount__lt=50))

    # 关联查询
    # 1. 通过书名查询人物
    # book = BookInfo.objects.get(pk=1)
    # print(book.peopleinfo_set.all())

    # 2. 通过人物查询书籍
    # person = PeopleInfo.objects.get(pk=1)
    # print(person.book.name)

    # 关联过滤查询(书籍查询人物)
    BookInfo.objects.filter(peopleinfo__name='郭靖')
    BookInfo.objects.filter(peopleinfo__description__contains='八')

    # 人物查询书籍
    PeopleInfo.objects.filter(book__name='郭靖')
    PeopleInfo.objects.filter(book__commentcount__gt=30)
    return render(request, 'book/index.html', context)
