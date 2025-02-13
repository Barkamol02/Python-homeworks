# Ask the user to enter a password.
# If the password is shorter than 8 characters, print "Password is too short."
# If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.".
# If the password meets both criteria, print "Password is strong."

password =str(input("Please enter password: "))

if len(password)<8:
    print("Password is too short.")
elif password == password.lower():
    print("Password must contain an uppercase letter.")
else:
    print("Your password is strong")    
     
