#a = "a" , "u" , "o" , "i" , "e"
#b = input("enter:")
#for i in b:
#    if i not in a:
#        print(i)
a = input()
b = "ауеиюяыэо"
for c in b:
    new = f'{c}к{c}'
    a = a.replace(c,new)
    if c not in b:
        print(c)
print(a)




