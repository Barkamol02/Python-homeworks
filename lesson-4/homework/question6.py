# Prime Numbers Task: Write a Python program that prints all prime numbers between 1 and 100.
prime = []
for i in range(1, 101):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime.append(i)

print(prime)
    