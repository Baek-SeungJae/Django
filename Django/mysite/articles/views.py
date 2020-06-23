from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from articles.models import Article, Comment
from .form import ArticleForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    articles = Article.objects.all()
    for i in range(len(articles)):
        articles[i].comment_count = len(
            Comment.objects.filter(article=articles[i]))

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
def new(request):
    return render(request, 'articles/new.html')


@login_required
def create(request):
    form = ArticleForm(request.POST, request.FILES)
    if form.is_valid():
        article = form.save(commit=False)
        article.user=request.user
        article.save()
    return redirect('articles:index')


@login_required
def detail(request, no):
    article = Article.objects.get(id=no)
    comments = article.comment_set.all()
    print(article.image)
    article.comment_count = len(Comment.objects.filter(article=article))
    commentform = CommentForm()
    context = {
        'article': article,
        'commentform': commentform,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
@require_POST
def delete(request, no):
    Article.objects.get(id=no).delete()
    return redirect('articles:index')


@login_required
def update(request, no):
    context = {
        'no': no,
        'title': Article.objects.get(id=no).title,
        'content': Article.objects.get(id=no).content,
    }
    return render(request, 'articles/update.html', context)


@login_required
@require_POST
def updated(request):
    no = int(request.POST.get('no'))
    article = Article.objects.get(id=no)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', no)


@login_required
@require_POST
def newComment(request, no):
    article = Article.objects.get(id=no)
    Comment.objects.create(
        article=article, content=request.POST.get('content'), user=request.user)
    return redirect('articles:detail', no)


@login_required
@require_POST
def deleteComment(request, no):
    comment = Comment.objects.get(id=request.POST.get('commentId'))
    comment.delete()
    return redirect('articles:detail', no)


@login_required
@require_POST
def updateComment(request, no):
    comment = Comment.objects.get(id=request.POST.get('commentId'))
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid():
        comment = form.save()
    return redirect('articles:detail', no)


@login_required
def like(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    user = request.user
    if user in article.like_users.all():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)

    return redirect('articles:index')