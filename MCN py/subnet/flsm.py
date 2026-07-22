import math

def ip_to_int(ip):
    octets = list(map(int, ip.split('.')))
    if len(octets) != 4 or any(o < 0 or o > 255 for o in octets):
        raise ValueError("Invalid IP address")
    return sum(octets[i] << (24 - 8 * i) for i in range(4))


def int_to_ip(value):
    return ".".join(str((value >> shift) & 255) for shift in (24, 16, 8, 0))


def mask_from_cidr(cidr):
    if cidr < 0 or cidr > 32:
        raise ValueError("CIDR must be between 0 and 32")
    mask_bits = '1' * cidr + '0' * (32 - cidr)
    return [int(mask_bits[i:i + 8], 2) for i in range(0, 32, 8)]


ip_input, cidr, subnet_count = input(
    "Enter IP, CIDR, and number of subnets (e.g., 225.225.1.10 26 4): "
).split()
cidr = int(cidr)
subnet_count = int(subnet_count)

if subnet_count <= 0:
    raise ValueError("Number of subnets must be positive")

subnet_bits = math.ceil(math.log2(subnet_count))
new_cidr = cidr + subnet_bits
if new_cidr > 32:
    raise ValueError("Too many subnets for this network")

base_mask = mask_from_cidr(cidr)
octets = list(map(int, ip_input.split('.')))
network_octets = [octets[i] & base_mask[i] for i in range(4)]
network_int = ip_to_int(".".join(map(str, network_octets)))

block_size = 1 << (32 - new_cidr)
total_subnets = 1 << subnet_bits

print("New Mask:", ".".join(map(str, mask_from_cidr(new_cidr))))
print("Number of subnets created:", total_subnets)

for i in range(total_subnets):
    subnet_network_int = network_int + i * block_size
    subnet_broadcast_int = subnet_network_int + block_size - 1
    print(f"Subnet {i + 1}:")
    print("  Network:   ", int_to_ip(subnet_network_int))
    print("  Broadcast: ", int_to_ip(subnet_broadcast_int))