#1
username = input("Enter username:")
password = input("Enter password:")
if password and username:
    print("welcome")
else:
    print("please enter both username and password")    

#2
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
print(a==b) #checks if 2 numbers are equal

#3
print(0<a) #checks if a is positive
print(a%2==0) #checks if a is even

#4
c=int(input("Enter number for c:"))
print(a!=b and b!=c and a!=c) #checks if all numbers are different

#5
string1 = input("Enter a string:")
string2 = input("Enter another string:")
length1 = len(string1)
length2 = len(string2)
print(length1==length2) #checks if length of both strings are equal

#6
print(a%3==0 and a%5==0) #checks if a is divisible by 3 and 5

#7
print(a+b>50.8) #checks if sum of a and b is greater than 50.8
print(10<=a<=20) #checks if a is between 10 and 20
