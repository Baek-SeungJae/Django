from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from articles_2.models import Article_2
# Create your views here.


def index(request):
    articles = Article_2.objects.all()
    article_list = list()
    for i in range(len(articles)):
        article_list.append(articles[i])
    context = {
        'article_list': article_list,
    }

    return render(request, 'articles_2/index.html', context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
        return redirect('articles_2:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles_2/form.html', context)


def update(request, article_pk):
    article = get_object_or_404(Article_2, id = article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            article = form.save()
        return redirect('articles_2:index')
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'articles_2/form.html', context)



def detail(request, article_pk):
    print(dir(request.resolver_match))
    article = get_object_or_404(Article_2, id = article_pk)
    context = {
        'article':article,
    }
    return render(request, 'articles_2/detail.html', context)

