import math

def ip_to_int(ip_str):
    octets = list(map(int, ip_str.split('.')))
    return (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]

def int_to_ip(ip_int):
    return f"{(ip_int >> 24) & 255}.{(ip_int >> 16) & 255}.{(ip_int >> 8) & 255}.{ip_int & 255}"

base_ip = input("Enter Base IP (e.g., 192.168.0.0): ")
n = int(input("Enter number of subnets: "))

hosts = sorted([int(input(f"Hosts for subnet {i+1}: ")) for i in range(n)], reverse=True)

current_ip_int = ip_to_int(base_ip)

print("\n--- Proper VLSM Allocation Table ---")
for req in hosts:
    size = 2 ** math.ceil(math.log2(req + 2))
    cidr = 32 - int(math.log2(size))
    
    mask = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF
    broadcast = current_ip_int + size - 1
    
    print(f"Subnet (Req: {req} hosts)")
    print(f"  Network:   {int_to_ip(current_ip_int)}/{cidr}")
    print(f"  Mask:      {int_to_ip(mask)}")
    print(f"  First IP:  {int_to_ip(current_ip_int + 1)}")
    print(f"  Last IP:   {int_to_ip(broadcast - 1)}")
    print(f"  Broadcast: {int_to_ip(broadcast)}\n")
    
    current_ip_int += size