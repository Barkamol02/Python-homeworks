def factor(n: int):
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")
number = int(input("Please enter a positive integer: "))
factor(number)