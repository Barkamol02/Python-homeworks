def invest(amount, rate , years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

principal = float(input("Initial amount: "))
rate = float(input("Yealy rate of return: "))
years = int(input("Number of years: ")) 
invest(principal, rate, years)      