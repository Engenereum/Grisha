#t1 = input("Ввод:")
#if len(t1) < 6:
 #   print("Длинна меньше 6")
#elif len(t1) >= 6:
 #   print(t1[5])

#str1 = "привет мир"
#substr = "привет"
#if substr in str1:
 #   print("a")

t1 = input("Введите город:").lower()
t2 = input("Введите второй город:").lower()
if t1[-1] == t2[0]:
    print("Верно")
else:
    print("Ошибка")
