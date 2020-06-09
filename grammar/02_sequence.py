# 데이터가 순차적으로 나열되어 있다.
# 정렬되어있다는 뜻은 아님
# list, tuple, range, string

# 1. list
list_a = []
list_b = list()
list_a = ['삼성',23,True]
print(list_a[-1])

# 2. tuple
tuple_a = ()
# tuple_b = tuple() 형태는 안된다.
tuple_a = (1,2,3,4)
print(tuple_a)

# 3. range
print(range(10))
print(type(range(10)))
print(list(range(10)))
print(list(range(3,10,2)))