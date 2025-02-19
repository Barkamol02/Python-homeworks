import os

def add_employee():
    with open("employees.txt", "a") as file:
        data = input("Enter employee details (ID, Name, Position, Salary): ")
        file.write(f"{data}\n")
    print("Employee record added successfully!\n")

def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            if records:
                print("Employee Records:")
                for record in records:
                    print(record.strip())
            else:
                print("No employee records found.")
    except FileNotFoundError:
        print("No employee records found.")
    print()

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            for record in records:
                if record.startswith(emp_id + ","):
                    print("Employee Found:", record.strip())
                    return
        print("Employee not found.")
    except FileNotFoundError:
        print("No employee records found.")
    print()

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
        updated_records = []
        found = False
        for record in records:
            if record.startswith(emp_id + ","):
                data = input("Enter new employee details (ID, Name, Position, Salary): ")
                updated_records.append(f"{data}\n")
                found = True
            else:
                updated_records.append(record)
        if found:
            with open("employees.txt", "w") as file:
                file.writelines(updated_records)
            print("Employee record updated successfully!")
        else:
            print("Employee not found.")
    except FileNotFoundError:
        print("No employee records found.")
    print()

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
        updated_records = [record for record in records if not record.startswith(emp_id + ",")]
        if len(updated_records) < len(records):
            with open("employees.txt", "w") as file:
                file.writelines(updated_records)
            print("Employee record deleted successfully!")
        else:
            print("Employee not found.")
    except FileNotFoundError:
        print("No employee records found.")
    print()

def main():
    while True:
        print("Employee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ")
        print()
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
