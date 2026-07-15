import random

frames = int(input("Enter total frames: "))
curr = 1

while curr <= frames:
    print(f"Sending Frame {curr}...")
    if random.random() > 0.25:
        print(f"ACK received for Frame {curr}.\n")
        curr += 1
    else:
        print(f"ACK lost. Retransmitting Frame {curr}...\n")