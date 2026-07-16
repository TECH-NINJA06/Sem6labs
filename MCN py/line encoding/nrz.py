import matplotlib.pyplot as plt

data = input("Enter binary string (e.g., 10110): ")

t_nrz = list(range(len(data) + 1))
nrz_l = [1 if b == '1' else -1 for b in data]
nrz_l.append(nrz_l[-1])

plt.figure(figsize=(10, 3))
plt.title(f"NRZ-L for '{data}'", fontsize=14)
plt.step(t_nrz, nrz_l, where='post', color='blue', linewidth=2.5)
plt.ylim(-1.5, 1.5)
plt.yticks([-1, 0, 1], ['Low', '0', 'High'])
plt.xticks(t_nrz)
plt.grid(True, axis='x', linestyle='--', color='gray')
plt.tight_layout()
plt.show()