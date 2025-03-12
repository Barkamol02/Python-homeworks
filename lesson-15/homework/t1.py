import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 - 4*x + 4

x = np.linspace(-10, 10, 500)
y = f(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x) = x² - 4x + 4', color='blue')
plt.title('Plot of f(x) = x² - 4x + 4', fontsize=14)
plt.xlabel('x values', fontsize=12)
plt.ylabel('f(x) values', fontsize=12)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()
