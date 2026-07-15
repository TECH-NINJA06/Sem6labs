user_input = input("Enter data segments (space separated): ")
data = list(map(int, user_input.split()))
s = sum(data)

checksum = ~s & 0xFF 

print(f"Sum: {s}")
print(f"Generated Checksum: {checksum}")