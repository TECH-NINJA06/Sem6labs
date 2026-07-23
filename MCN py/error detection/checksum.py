user_input = input("Enter data segments (space separated): ")
sender_checksum = int(input("Enter sender checksum: "))
data = list(map(int, user_input.split()))
s = sum(data)

checksum = ~s & 0xFF 

if checksum == sender_checksum:
    print("Checksum is valid. Data received successfully.")
else:
    print("Checksum is invalid. Data may be corrupted.")