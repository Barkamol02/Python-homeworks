import csv


grades = []
with open('grades.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['Grade'] = int(row['Grade'])
        grades.append(row)

subjects = {}
for grade in grades:
    subject = grade['Subject']
    if subject not in subjects:
        subjects[subject] = []
    subjects[subject].append(grade['Grade'])

average_grades = {subject: sum(grades) / len(grades) for subject, grades in subjects.items()}

with open('average_grades.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Subject', 'Average Grade'])
    for subject, average in average_grades.items():
        writer.writerow([subject, average])

print ("Process completed Successfully")
