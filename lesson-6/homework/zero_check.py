with open("employees.txt", 'w') as file:
    #records = input("Enter the employee records: ")
    #record_list = [word.strip() for word in records.split(',')]
    #emp_id = int(record_list[0])
    #emp_name = record_list[1]
    #emp_position = record_list[2]
    #emp_salary = int(record_list[3])
    #file.writelines(records)
    pass

def Add_record(data):
    with open("employees.txt", 'a') as file:
        file.write(data + "\n")

def view_record():
    with open("employees.txt", 'r') as file:
        print("".join(file.readlines()))

def search_record(with_id):
    with open("employees.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            record_list = [word.strip() for word in line.split(',')]
            emp_id = int(record_list[0])
            
            if emp_id == with_id:
                return line

        else:
            return False

def update_record(with_ID):
    if search_record(with_ID) == False:
        print("No such empployee")
    else:
        with open("employees.txt", 'r') as file:
            lines = file.readlines()
        with open("employees.txt", 'w') as file:
            for line in lines:
                if line.startswith(str(with_ID) + ","):
                    up_name = input("Enter updated name: ")
                    up_position = input("Enter updated position: ")
                    up_salary = int(input("Enter updated salary: "))
                    file.write(f"{with_ID}, {up_name}, {up_position}, {up_salary}\n")
                else:
                    file.write(line)

def del_record(with_Id):
    if search_record(with_Id) == False:
        return("No such empployee")
    else:
        with open("employees.txt", 'r') as file:
            lines = file.readlines()
        with open("employees.txt", 'w') as file:
            for line in lines:
                if line.startswith(str(with_Id) + ","):
                    pass
                else:
                    file.write(line)







answer = 1
print("""Option 1: Append a new employee record to "employees.txt".
Option 2: Display all employee records from "employees.txt".
Option 3: Allow the user to search for an employee by Employee ID and display their details.
Option 4: Update an employee’s information (name, position, or salary) based on the Employee ID.
Option 5: Delete an employee's record from the file using the Employee ID.
Option 6: Exit the program.""")
while answer != 6:
    answer = int(input("Choose one of the options: "))
    if answer == 1:
        data = input("Enter the employee record as 'employee_ID, emp_name, emp_pos, emp_salary': ")
        Add_record(data)
    elif answer == 2:
        view_record()
    elif answer == 3:
        IDD = int(input("Enter the Id you want to search: "))
        print(search_record(IDD))
    elif answer == 4:
        IDD = int(input("Enter the Id you want to update: "))
        update_record(IDD)
    elif answer == 5:
        IDD = int(input("Enter the Id you want to delete: "))
        del_record(IDD)
    elif answer == 6:
        pass
    else:
        print("There is no such option. Try again")