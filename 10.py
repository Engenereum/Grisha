fname = input()
f = open(fname, encoding='utf-8')
src = f.read()
words = src.split(' ')
res = {}
for word in words:
    word = word.replace('(','').replace(')','').strip().lower()
    if word == '':
        continue
    if word in res.keys():
        res[word] += 1
    else:
        res[word] = 1


max_repeat = max(res.values())
for k,v in res.items():
    if v == max_repeat:
        print(k,v)
        break

print(max_repeat)


pass