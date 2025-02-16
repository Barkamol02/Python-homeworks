def  enrollment(univer):
    fees = []
    totals = []
    for item in univer:
        university, total, fee = item
        totals.append(total)
        fees.append(fee)
    return totals, fees

def mean(list1):
    return (sum(list1))/(len(list1))

def meadian(list2):
    if len(list2) % 2 == 1:
        return((sorted(list2))[len(list2)//2])
    else:
        return (((sorted(list2))[len(list2)//2]) + ((sorted(list2))[len(list2)//2-1]))/2

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
num_students, tuitions = enrollment(universities)
student_mean = round(mean(num_students), 2)
student_median = meadian(num_students)
tuition_mean = round(mean(tuitions), 2)
tuition_median = meadian(tuitions)
print("******************************")
print(f"Total students: {sum(num_students): ,}")
print(f"Total tuition: $ {sum(tuitions):,}")
print("")
print(f"Student mean: {student_mean:,}")
print(f"Student median: {student_median:,}")
print("")
print(f"Tuition mean: $ {tuition_mean:,}")
print(f"Tuition median: $ {tuition_median:,}")
print("******************************")