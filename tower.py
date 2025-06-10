height = int(input())
width = 2 * height - 1
for i in range(1, height + 1):
    stars = 2 * i - 1
    spaces = (width - stars) // 2
    print(" " * spaces + "*" * stars + " " * spaces)
