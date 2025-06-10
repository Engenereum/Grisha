m = [3,4,2,5,2,3,4,5]
print(m[0])
print(m[1])
print(min(m))
print(max(m))
print(sum(m))
print(sum(m)/len(m))
print(sorted(m))
m.sort()
print(m)
#s = input("Введите свои оценки через пробел:")
#d = s.split(" ")
#for i in range(0, len(d), 1):
#    d[i] = int(d[i])
#print(d)
#itog = sum(d)//len(d)

#if itog == 2:
#    print("Ученик является двоечником")
#if itog == 3:
#    print("Ученик является троечником")
#if itog == 4:
#    print("Ученик является хорошистом")
#if itog == 5:
#    print("Ученик является отличником")


list1 = [4,5,2,7]
list2 = [2,6,8,1]
list3 = list1+list2
print(sorted(list3))
list4 = [1,1,1,1]
list5 = [2,2,2,2]
list6 = list4+list5
print(sorted(list6))
l1 = [4,5,2,7]
l2 = [2,6,8,1]
l1.sort()
l2.sort()
for i in range(len(l1)):
    print(l1[i])
    print(l2[i])

j = input(":")
j2 = input(":")
jj = j.split(",")
jj2 = j2.split(",")
if jj > jj2:
    print(jj)
    print("список 1 длиннее")
elif jj2 > jj:
    print(jj2)
    print("список 2 длиннее")
n = input(":")
nn = n.split(" ")
for nnn in nn:
    print('*' * int(nnn))