
#while True:
  #  t1 = input("Введите пароль:")
#if len(t1) < 8:
   ##     print("Короткий пароль")
   #     continue
  #  if "123" in t1:
    #    print("Простой пароль")
  #  else:
        #print("OK")
  #      exit()
t1 = ""
while (len(t1) < 8) or ("123" in t1):
    t1 = input("Введите пароль:")