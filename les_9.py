src="лвоаоыфщшырмчсдлцтыдвлмячст"
chars = []
counts = []
for ch in src:
    if ch in chars:
        index = chars.index(ch)
        counts[index]+=1
    else:
     chars.append(ch)
     counts.append(1)
for index in range(len(chars)):
    print(f'{chars[index]} - {counts[index]}')





