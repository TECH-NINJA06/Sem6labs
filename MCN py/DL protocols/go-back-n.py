import random

frames, window = map(int, input("Enter frames and window size (e.g. 10 3): ").split())
i = 1

while i <= frames:
    current_window = list(range(i, min(i + window, frames + 1)))
    print(f"Sending window: {current_window}")
    
    lost_frame = 0
    for j in current_window:
        if random.random() < 0.2: 
            print(f"ACK lost for {j}. Going back.")
            lost_frame = j
            break
        print(f"ACK received for {j}")
        
    if lost_frame == 0:
        i += window
    else:
        i = lost_frame
    print("-" * 20)