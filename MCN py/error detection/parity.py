d = list(map(int, input("Enter 4 data bits (space separated): ").split()))
parity = input("Enter parity mode (even/odd): ").strip().lower()

p1 = d[0] ^ d[1] ^ d[3]
p2 = d[0] ^ d[2] ^ d[3]
p4 = d[1] ^ d[2] ^ d[3]

if parity == 'odd':
    p1 ^= 1
    p2 ^= 1
    p4 ^= 1

print(f"Final Transmitted Sequence: {p1} {p2} {d[0]} {p4} {d[1]} {d[2]} {d[3]}")