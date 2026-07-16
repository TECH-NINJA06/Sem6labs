import matplotlib.pyplot as plt

data = input("Enter binary string (e.g., 10110): ")

t_nrz = list(range(len(data) + 1))
nrz_i = []
curr = 1

for b in data:
    if b == '1':
        curr = -curr
    nrz_i.append(curr)

nrz_i.append(nrz_i[-1])

plt.figure(figsize=(10, 3))
plt.title(f"NRZ-I for '{data}'", fontsize=14)
plt.step(t_nrz, nrz_i, where='post', color='red', linewidth=2.5)
plt.ylim(-1.5, 1.5)
plt.yticks([-1, 0, 1], ['Low', '0', 'High'])
plt.xticks(t_nrz)
plt.grid(True, axis='x', linestyle='--', color='gray')
plt.tight_layout()
plt.show()