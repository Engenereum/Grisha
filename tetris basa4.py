text1 = input("Первый игрок,Введите Камень,Ножницы или Бумага:")
text2 = input("Второй игрок,Введите Камень,Ножницы или Бумага:")
a = None
if text1 in ["Камень" , "Ножницы" , "Бумага"]:
    pass
else:
    print("Неизвестный жест")
    exit(1)
if text2 in ["Камень", "Ножницы", "Бумага"]:
    pass
else:
    print("Неизвестный жест")
    exit(1)
if text1 == text2:
    print("Ничья")
else:
    if text1 == "Камень" and text2 == "Ножницы":
        a = True
        if text1 == "Ножницы" and text2 == "Бумага":
            a = True
            if text1 == "Бумага" and text2 == "Камень":
                a = True
            else:
                a = False
if a:
    print("Первый игрок победил")
if not a:
    print("Второй игрок победил")
