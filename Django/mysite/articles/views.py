from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    return render(request, 'articles/index.html')


def new(request):
    return render(request, 'articles/new.html')


@csrf_exempt
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    context = {
        'title':title,
        'content':content,
    }
    return render(request,'articles/create.html',context)

