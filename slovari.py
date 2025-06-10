dictionary = {0: 'Первый элемент', 1: 'второй элемент'}
print(dictionary)
print(dictionary[0])
print(dictionary[1])
dictionary[2] = 'element'
print(dictionary[2])
del dictionary[1]
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
for key, value in dictionary.items():
    print(key, value)

# res = {}
# for ch in src:
#    if ch in list(res.keys()):
#        res[ch] += 1
#    else:
#        res[ch] = 1
# print(res)
src = "лво3аоы4фщш1ырмчсдлцты5дв0лмя89чст"
r = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
n = range(1, 10)
count = {}
for c in src:
    if c in list(r.values()):
        if c not in count.keys():
            count[c] = 0
        count[c] += 1
print(count)

books = {'Math': 12, 'Rus': 104, 'His': 17}
print(books)
a = books['Math']
a2 = books['Rus']
a3 = books['His']
print(a+a2+a3)
sub = ""
res = 99999

for y in books.keys():
    if books[y] <= res:
        sub = y
        res = books[y]

print(sub)

f = open("list.py",encoding='utf-8')
src = f.read()
print(src)
f.close()
f = open("test.txt", mode='a')
f.write("123456789")
f.close()

