from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'name': 'hahaha876tr',
    }
    return render(request, 'book/index.html', context)
