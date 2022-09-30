from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'name': '姓名啊',
    }
    return render(request, 'book/index.html', context)
