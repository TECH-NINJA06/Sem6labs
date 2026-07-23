data = input("Enter binary string (e.g., 10110): ")

diff_man = []
curr = 1

for b in data:
    if b == '0':
        curr = -curr
    diff_man.append(curr)

    curr = -curr
    diff_man.append(curr)

print(diff_man)