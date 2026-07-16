data = input("Enter Data bits: ")
gen = input("Enter Generator bits: ")

div = list(data + '0' * (len(gen) - 1))

for i in range(len(data)):
    if div[i] == '1':
        for j in range(len(gen)):
            div[i+j] = str(int(div[i+j]) ^ int(gen[j]))

crc = "".join(div)[-(len(gen)-1):]
print(f"Generated CRC: {crc}")
print(f"Transmitted Data: {data + crc}")