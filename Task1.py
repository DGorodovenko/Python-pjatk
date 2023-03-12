numbs = [256, 81, 256, 82, 27, 16807, 456]
divis = [16, 3, 8, 9, 3, 7, 4]

for n, d in zip(numbs, divis):
    if n % d == 0:
        x = n // d
        while x % d == 0:
            x //= d
        if x == 1:
            print(f"{n} is a power of {d}")
        else:
            print(f"{n} is not a power of {d}")
    else:
        print(f"{n} is not divisible by {d}")