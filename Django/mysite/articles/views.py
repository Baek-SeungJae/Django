from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from articles.models import Article
# Create your views here.


def index(request):
    content = Article.objects.all()
    n = list(range(len(content)))
    article = list()
    for i in n:
        article.append(content[i])
    context = {
        'content': content,
        'n': n,
        'article': article
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    Article.objects.create(title=title, content=content)
    context = {
        'title': title,
        'content': content,
    }
    return redirect('articles:index')


def detail(request, no):
    article = Article.objects.get(id=no)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


def delete(request, no):
    if request.method == 'POST':
        Article.objects.get(id=no).delete()
    return redirect('articles:index')


def update(request, no):
    context = {
        'no': no,
        'title': Article.objects.get(id=no).title,
        'content': Article.objects.get(id=no).content,
    }
    return render(request, 'articles/update.html', context)


def updated(request):
    if request.method == 'POST':
        no = int(request.POST.get('no'))
        print(no)
        article = Article.objects.get(id=no)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
    return redirect('articles:detail',no)
