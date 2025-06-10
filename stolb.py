#a = int(input())
#for b in range(1,10):
 #   f = f"{b} * {a} = {a*b}"
 #   print(f)

for i in range(1,11,2):
    for j in range(1,11,):
        if i == 9 and j == 10:
            print(f"#\t{i} * {j} = {j*i}\t#\t{i+1} * {j} = {(i+1)*j}\t#")
            continue
        print(f"#\t{i} * {j} = {j*i}\t#\t{i+1} * {j} = {(j)*(i+1)}\t\t#")

    print("+##################################+")

