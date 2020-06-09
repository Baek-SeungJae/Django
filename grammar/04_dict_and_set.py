# 1. dictinary
# 1. dictinary
# key, value로 이루어져 있음
dict_a = {}
dict_b = dict()
dict_a = {'삼성':100,'역삼':30,'삼성':50}
print(dict_a)
print(dict_a['삼성'])
print(dict_a.get('삼성ㅁ'))
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())

# 2. set
set_a = {1,3,2}
set_b = set()
set_b = {3,6,8}

print(set_a - set_b)
print(set_a & set_b)

list_a = [1,1,1,1]
print(list(set(list_a))[0])
set_b.copy