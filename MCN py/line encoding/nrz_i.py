data = input("Enter binary string (e.g., 10110): ")

nrz_i = []
curr = 1

for b in data:
    if b == '1':
        curr = -curr
    nrz_i.append(curr)

print(nrz_i)


# def plot_ascii(name, bits, voltages):
#     print(f"\n=== {name} ===")

#     bit_line = "Bits:  "
#     for b in bits:
#         bit_line += f" {b} "
#     print(bit_line)

#     high_line = "High:  "
#     for v in voltages:
#         high_line += "---" if v == 1 else "   "
#     print(high_line)

#     low_line = "Low:   "
#     for v in voltages:
#         low_line += "   " if v == 1 else "___"
#     print(low_line)


# plot_ascii("NRZ-I", data, nrz_i)