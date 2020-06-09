for i in range(0,10,1):
    if i%2 == 0: 
        print(i)


# for_dictionary

dict_a = {
    '삼성' : 100,
    '역삼' : 50,
    '선릉' : 30
}

print(dict_a)

for key,val in dict_a.items():
    print(key,val)