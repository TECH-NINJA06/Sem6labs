ip_input, cidr = input("Enter IP and CIDR (e.g., 225.225.1.10 26): ").split()
cidr = int(cidr)
octets = list(map(int, ip_input.split('.')))

mask_bits = '1' * cidr + '0' * (32 - cidr)
mask = [int(mask_bits[i:i+8], 2) for i in range(0, 32, 8)]

net = [octets[i] & mask[i] for i in range(4)]
brd = [net[i] | (255 - mask[i]) for i in range(4)]

print("Mask:      ", ".".join(map(str, mask)))
print("Network:   ", ".".join(map(str, net)))
print("Broadcast: ", ".".join(map(str, brd)))