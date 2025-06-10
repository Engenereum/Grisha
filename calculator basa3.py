
text1 = int(input("Введите первое число:"))
text2 = int(input("Введите второе число:"))
text3 = input("Введите производимую операцию:")
if text3 == "+":
    print(text1 + text2)
if text3 == "-":
    print(text1 - text2)
if text3 == "*":
    print(text1 * text2)
if text3 == "/" and text2 != 0:
    print(text1 / text2)
if text3 == "//" and text2 != 0:
    print(text1 // text2)
if text3 == "**":
    print(text1 ** text2)
else:
   print("Неизвестная операция")
