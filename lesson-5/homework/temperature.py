def convert_cel_to_far(cel):
    return round(cel * 9/5 + 32, 2)
def convert_far_to_cell(far):
   return round((far-32)*5/9, 2)

far = float(input("Enter a temperature in degrees F: "))
cel = float(input("Enter a temperature in degrees C: "))
print(far, "degrees F: ", convert_far_to_cell(far), "degrees in C")
print(cel, "degrees C: ", convert_cel_to_far(cel), "degrees in F")


