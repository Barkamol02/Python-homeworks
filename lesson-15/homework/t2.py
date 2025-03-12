import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y_sin, label='sin(x)', color='red', linestyle='-', marker='o', markevery=50)
plt.plot(x, y_cos, label='cos(x)', color='blue', linestyle='--', marker='s', markevery=50)

plt.title('Plot of sin(x) and cos(x)', fontsize=14)
plt.xlabel('x values', fontsize=12)
plt.ylabel('Function values', fontsize=12)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()
