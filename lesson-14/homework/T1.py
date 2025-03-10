import numpy as np

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

convert = np.vectorize(f_to_c)

temps_f = [32, 68, 100, 212, 77]
temps_c = convert(temps_f)

print(temps_c)
