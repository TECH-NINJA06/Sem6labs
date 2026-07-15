import random

frames, window = map(int, input("Enter frames and window size: ").split())
acked = [False] * (frames + 1)
i = 1

while i <= frames:
    current_window = range(i, min(i + window, frames + 1))
    
    for j in current_window:
        if not acked[j]: print(f"Sending Frame {j}")
        
    for j in current_window:
        if not acked[j]:
            if random.random() > 0.2:
                print(f"ACK received for {j}")
                acked[j] = True
            else:
                print(f"ACK lost for {j}. Will repeat.")
                
    while i <= frames and acked[i]:
        i += 1
    print("-" * 20)