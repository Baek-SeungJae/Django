# 01_operations.py
# 논리연산자
# and, or, not

T = True
F = False

print("___AND___")
print(T and T)
print(T and F)
print(F and T)
print(F and F)

print("___OR___")
print(T or T)
print(T or F)
print(F or T)
print(F or F)

print("___NOT___")
print(not T)
print(not F)

# in, not in
print("___IN___")
print('a' in 'apple')
print(1 not in [1,2,3]) 

# 단축평가
print('' or 'Text' or 'Text2')
print('Text' and '' or 'Text2')