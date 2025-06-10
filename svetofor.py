red = "красный"
yellow = "желтый"
green = "зеленый"
q1 = "1"
q2 = "2"
q3 = "3"
prov = None
userred = input("Введите цвет 1:")
useryellow = input("Введите цвет 2:")
usergreen = input("Введитецвет 3:")
if (userred == red or userred==q1) and (useryellow == yellow or useryellow==q2) and (usergreen == green or usergreen==q3):
    prove = True
else:
    prove = False
if prove:
    print("ПОЕХАЛИ")
else:
    print("СТОЙ")
