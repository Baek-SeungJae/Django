from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'login.html')


def static_example(request):
    return render(request, 'static_example.html')
