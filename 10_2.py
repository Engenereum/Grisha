def func():
    return 'Grisha'
print(func())


def func2(n1,n2):
    return n1+n2

n1 = 1
n2  = -8
print(func2(n1,n2))
print(func2(5,4))

def func3(a,b,z):
    if z == "+":
        return a+b
    if z == "-":
        return a-b
    if z == "*":
        return a*b
    if z == "**":
        return a**b
    if z == "/":
        return a/b
    if z == "//":
        return a//b
print(func3(2,2,'-'))

def funcstr(str1,str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str1) < len(str2):
        print(str2)

str1 = 'asdfexx'
str2 = 'sd,fskgewgkfd'
funcstr(str1,str2)

def rat(str,s):
    count = 0
    for char in str:
        if s == char:
            count += 1
        else:
            continue
    return count
c = rat('azazaldlsdfgmefksdda','a')
print(c)

def lastfunc(k):
    print(len(k))
lastfunc(('lkasdmnflkasbnd',))