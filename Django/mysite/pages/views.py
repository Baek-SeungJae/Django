from django.shortcuts import render
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import random
from hanspell import spell_checker
from articles.models import Article
# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def hello(request):
    menu = ['닭갈비', '탕수육', '초밥', '스파게티돈가스']
    pick = random.choice(menu)
    return render(request, 'pages/hello.html', {'pick': pick})


def name(request):
    my_name = "부러럭"
    return render(request, 'pages/name.html', {'my_name': my_name})


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
    return render(request, 'pages/introduce.html', context)


def yourname(request, name):
    return render(request, 'pages/yourname.html', name)


def nameAndAge(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'pages/nameAndAge.html', context)


def multiply(request, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    context = {
        'num1': num1,
        'num2': num2,
        'result': num1*num2,
    }
    return render(request, 'pages/multiply.html', context)


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
    return render(request, 'pages/googoodan.html', context)


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
    return render(request, 'pages/dtl.html', context)


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
    return render(request, 'pages/forif.html', context)


@csrf_exempt
def catch(request):
    msg = request.POST.get('msg')
    print(msg)
    context = {
        'msg': msg
    }
    return render(request, 'pages/catch.html', context)


def throw(request):
    return render(request, 'pages/throw.html')


def urlexam(request, name):
    my_list = ['짜장면', '차돌짬뽕', '탕수육', '콩국수']
    lunch = random.choice(my_list)
    context = {
        'name': name,
        'lunch': lunch,
    }
    return render(request, 'pages/urlexam.html', context)


def wordtest(request):
    content = Article.objects.filter(title__contains='').last().content
    result = spell_checker.check(u'반도체설계부터 공정 및 Platform생산할수 있는 인프라를 갖췄고 제품이나 새로운 기술을 좋아하기 때문입니다. AP 10nm Finfet을 넘어 7nm에 도전하여 기술로써 인류에 공헌하는 모습에 매료되었습니다. 2016년 4월 28일 화성캠퍼스내에서 System LSI사업부 Job Fair에 참석하여 직무에 대한 정보를 알 수 있었고 파운드리 사업부에서 어떤 일을 하는지에 대해 알 수 있었습니다. 4차 산업혁명이 도래함에 따라서 포화상태인 메모리 반도체 쪽보다 시스템반도체의 가능성이 컸기 때문에 지원했습니다. 단순히 모바일에 국한한 것이 아니라 오토모티브나 웨어러블으로 플랫폼의 응용이 무궁무진하다는 것이 시스템반도체의 매력을 느꼈기 때문입니다.')
    result = result.as_dict()
    words = result.get('words')
    original = result.get('original')
    checked = result.get('checked')
    l = list()
    for data in words:
        if words.get(data) != 0:
            l.append(data)

    context = {
        'result': result,
        'original': original,
        'checked': checked,
        'words': words,
        'content':content,
        'l': l
    }

    return render(request, 'pages/word.html', context)


def lotto(request):
    n = int(request.GET.get('n'))
    ranges = range(0, n, 1)
    lotto = list()
    for i in ranges:
        data = random.sample(range(1, 46), 6)
        data.sort()
        lotto.append(data)
    context = {
        'n': n,
        'lotto': lotto
    }
    return render(request, 'pages/lotto.html', context)
