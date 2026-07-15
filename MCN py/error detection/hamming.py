r = list(map(int, input("Enter 7 received bits (space separated): ").split()))
mode = input("Enter parity mode (even/odd): ").strip().lower()

c1 = r[0] ^ r[2] ^ r[4] ^ r[6]
c2 = r[1] ^ r[2] ^ r[5] ^ r[6]
c4 = r[3] ^ r[4] ^ r[5] ^ r[6]

if mode == 'odd':
    c1 ^= 1
    c2 ^= 1
    c4 ^= 1

error_pos = (c4 * 4) + (c2 * 2) + (c1 * 1)

if error_pos == 0:
    print("Status: No error detected in received data.")
else:
    print(f"Status: Error detected at position {error_pos}.")
    
    r[error_pos - 1] ^= 1 
    print(f"Corrected Hamming Code: {' '.join(map(str, r))}")

print(f"Extracted Data Bits: {r[2]} {r[4]} {r[5]} {r[6]}")