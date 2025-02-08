# Number Data Type Questions
#q1
userInput = float(input("Enter float number:"))
roundedNumber = round(userInput, 2)
print(roundedNumber)

#q2
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

print ("Largest number is:", largest)
print ("Smallest number is:", smallest)

#q3 
km = float(input("Enter distance in kilometers:"))
meters = km * 1000
centermeters = km * 100000
print(str(meters) + " meters")
print(str(centermeters) + " centimeters")

#q4
divident = int(input("Enter divident:"))
divisor = int(input("Enter divisor:"))
quotient = divident // divisor
remainder = divident % divisor
print("Quotient is:", quotient, "Remainder is:", remainder)             

#q5
celcius = float(input("Enter temperature in celcius:"))
fahrenheit = (celcius * 9/5) + 32
print("Temperature in fahrenheit is:", fahrenheit)

#q6
number1 = int(input("Enter a number:"))
lastDigit = number1%10
print(lastDigit)

#q7
userInput1= int(input("Enter a number:"))
condition = userInput1%2
if condition == 0:
    print("Number is even")
else:
    print("Number is not even")
