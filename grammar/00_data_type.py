# 1. 출력해보기
print("hello world")

# 프로그래밍 언어의 기본 3가지
# 1. 변수 저장
number = 10
string = '10'
boolean = True

# 파이썬에는 값이 없음을 표현하는 None 타입이 존재

nothing = None


print(type(number))
print(string)
print(boolean)
print(type(nothing))

# 1-1. 숫자형
number = 10
float_num = 1.3
complex_num = (3+3j)
print (type(number), type(float_num), type(complex_num))

# 2. bool
print(type(True))
print(type(False))

# 0, 0.0, [], {}
print(False==0)

# 3. 문자형
# '', ""
greeing = 'hi'
name = "kim"
print(greeing,name)

# 문자열 입력받기
age = input("나이를 입력해 주세요. : ")
print(age)

#string interpolation
name = "kim"
print("안녕하세요", name)
print("안녕하세요 {} {}".format(name,age))
print(f'{name},{age}')

# 연산과 출력 형태 지정
pi = 3.141592
print(f'원주율은 {pi:.4}, 반지름 = 2 원의 넓이는 {pi*2*2}')