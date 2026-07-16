import matplotlib.pyplot as plt

data = input("Enter binary string (e.g., 10110): ")

t_man = [i / 2 for i in range(2 * len(data) + 1)]
man = []

for b in data:
    if b == '0':
        man.extend([1, -1])
    else:
        man.extend([-1, 1])

man.append(man[-1])

plt.figure(figsize=(10, 3))
plt.title(f"Manchester for '{data}'", fontsize=14)
plt.step(t_man, man, where='post', color='green', linewidth=2.5)
plt.ylim(-1.5, 1.5)
plt.yticks([-1, 0, 1], ['Low', '0', 'High'])
plt.xticks([i / 2 for i in range(2 * len(data) + 1)])
plt.grid(True, axis='x', linestyle='--', color='gray')
plt.tight_layout()
plt.show()