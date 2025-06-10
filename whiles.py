#index = 0
#while index < 10:
 #   print(index)
  #  index = index + 1

#name = ""
#while name != "Гриша":
 #   name = input("введите имя:")
#print("Привет,Гриша")

stop = ""
t1 = input("Введите город:").lower()
while stop not in [ "выйти" , "Выйти" , "Exit" , "exit" , "Выход" , "выход"]:
    t2 = input("Введите город:").lower()
    if t1[-1] == t2[0]:
        print("Ответ засчитан")
        t1 = t2
    else:
        print("Ответ не засчитан")
        stop = input("Продолжить? <exit - выход>")
