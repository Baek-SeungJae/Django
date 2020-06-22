from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from articles.models import Article, Comment
from .form import ArticleForm, CommentForm
from django.views.decorators.http import require_POST
# Create your views here.


def index(request):
    articles = Article.objects.all()
    for i in range(len(articles)):
        articles[i].comment_count = len(Comment.objects.filter(article=articles[i]))
    context = {
        'articles': articles,
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
    comments = article.comment_set.all()
    article.comment_count = len(Comment.objects.filter(article=article))
    commentform = CommentForm()
    context = {
        'article': article,
        'commentform': commentform,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, no):
    Article.objects.get(id=no).delete()
    return redirect('articles:index')


def update(request, no):
    context = {
        'no': no,
        'title': Article.objects.get(id=no).title,
        'content': Article.objects.get(id=no).content,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def updated(request):
    no = int(request.POST.get('no'))
    article = Article.objects.get(id=no)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', no)


@require_POST
def newComment(request, no):
    article = Article.objects.get(id=no)
    Comment.objects.create(
        article=article, content=request.POST.get('content'))
    return redirect('articles:detail', no)


@require_POST
def deleteComment(request, no):
    comment = Comment.objects.get(id=request.POST.get('commentId'))
    comment.delete()
    return redirect('articles:detail', no)


@require_POST
def updateComment(request, no):
    comment = Comment.objects.get(id=request.POST.get('commentId'))
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid():
        comment = form.save()
    return redirect('articles:detail', no)
