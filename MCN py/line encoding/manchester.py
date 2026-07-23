data = input("Enter binary string (e.g., 10110): ")

man = []

for b in data:
    if b == '0':
        man.extend([1, -1])
    else:
        man.extend([-1, 1])

print(man)