from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, CustomUserCreationForm
from articles.models import Article, Comment
from .models import User
# Create your views here.


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        auth_form = AuthenticationForm(request, request.POST)
        if auth_form.is_valid():
            auth_login(request, auth_form.get_user())
            return redirect('articles:index')
    else:
        auth_form = AuthenticationForm()
    context = {
        'auth_form': auth_form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')


@require_POST
def delete(request):
    request.user.delete()
    return redirect('articles:index')


@login_required
def update(request):
    user = request.user
    if request.method == "POST":
        #form = PasswordChangeForm(user, request.POST)
        form = CustomUserChangeForm(request.POST, instance=user)
        print(form)
        if form.is_valid():
            user = form.save()
            return redirect('articles:index')

    else:
        #form = PasswordChangeForm(user)
        form = CustomUserChangeForm(instance=user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def password(request):
    print(request.resolver_match.url_name)
    user = request.user
    if request.method == "POST":
        form = PasswordChangeForm(user, request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            return redirect('articles:index')

    else:
        form = PasswordChangeForm(user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    articles = Article.objects.filter(user=person)
    comments = Comment.objects.filter(user=person)
    print(comments)
    context = {
        'articles': articles,
        'comments': comments,
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

def follow(request, user_pk):
    
    i = request.user
    user = User.objects.get(pk=user_pk)
    if i != user:
        if i in user.followers.all():
            user.followers.remove(i)
        else:
            user.followers.add(i)
    print(user.followers.all())
    return redirect('accounts:profile',user.username)
