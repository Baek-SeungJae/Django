from django.shortcuts import render
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import random
# Create your views here.


def index(request):
    return render(request, 'index.html')


def hello(request):
    menu = ['닭갈비', '탕수육', '초밥', '스파게티돈가스']
    pick = random.choice(menu)
    return render(request, 'hello.html', {'pick': pick})


def name(request):
    my_name = "부러럭"
    return render(request, 'name.html', {'my_name': my_name})


def introduce(request):

    context = {
        'java': random.choice(range(1, 50, 5)),
        'html': random.choice(range(1, 50, 5)),
        'css': random.choice(range(1, 50, 5)),
        'spring': random.choice(range(1, 50, 5)),
        'python': random.choice(range(1, 50, 5)),
        'oracle': random.choice(range(1, 50, 5)),
        'mongoDB': random.choice(range(1, 50, 5)),
        'Django': random.choice(range(1, 50, 5)),
        'mybatis': random.choice(range(1, 50, 5)),
        'android': random.choice(range(1, 50, 5)),
    }
    return render(request, 'introduce.html', context)


def yourname(request, name):
    return render(request, 'yourname.html', name)


def nameAndAge(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'nameAndAge.html', context)


def multiply(request, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    context = {
        'num1': num1,
        'num2': num2,
        'result': num1*num2,
    }
    return render(request, 'multiply.html', context)


def googoodan(request, num1, num2):
    googoodan = list()
    num1 = int(num1)
    for i in range(1, num1, 1):
        element = ""
        element += str(num1)
        element += " * "
        element += str(i)
        element += " = "
        element += str(num1*i)
        element += ""
        googoodan.append(element)
    context = {
        'googoodan': googoodan,
    }
    return render(request, 'googoodan.html', context)


def dtl(request):
    my_list = ['짜장면', '차돌짬뽕', '탕수육', '콩국수']
    empty_list = []
    my_string = "Life is short, You need python"
    today = datetime.now()
    context = {
        'my_list': my_list,
        'empty_list': empty_list,
        'my_string': my_string,
        'today': today,
    }
    return render(request, 'dtl.html', context)


def forif(request):
    my_list = [100, 50, 30, 20, 10]
    my_string = "간단한 문자열"
    data_a = "첫번째 데이터"
    data_b = "두번째 데이터"
    data_a, data_b = data_b, data_a
    context = {
        'my_list': my_list,
        'my_string': my_string,
        'data_a': data_a,
        'data_b': data_b
    }
    return render(request, 'forif.html', context)

@csrf_exempt
def catch(request):
    msg = request.POST.get('msg')
    print(msg)
    context = {
        'msg':msg
    }
    return render(request, 'catch.html',context)

def throw(request):
    return render(request, 'throw.html')
