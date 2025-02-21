import json
import csv
import os

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
    
    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }
    
    @staticmethod
    def from_dict(data):
        return Task(data["task_id"], data["title"], data["description"], data.get("due_date"), data["status"])

class TaskManager:
    def __init__(self, storage):
        self.tasks = []
        self.storage = storage
    
    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
        status = input("Enter Status (Pending/In Progress/Completed): ")
        task = Task(task_id, title, description, due_date, status)
        self.tasks.append(task)
        print("Task added successfully!\n")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
            return
        print("Tasks:")
        for task in self.tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")
    
    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("Enter new Title: ")
                task.description = input("Enter new Description: ")
                task.due_date = input("Enter new Due Date (YYYY-MM-DD, optional): ") or None
                task.status = input("Enter new Status (Pending/In Progress/Completed): ")
                print("Task updated successfully!\n")
                return
        print("Task not found.\n")
    
    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!\n")
    
    def filter_tasks(self):
        status = input("Enter status to filter by (Pending/In Progress/Completed): ")
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print("No tasks found with the given status.\n")
        else:
            for task in filtered_tasks:
                print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")
    
    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved successfully!\n")
    
    def load_tasks(self):
        self.tasks = self.storage.load()
        print("Tasks loaded successfully!\n")

class JSONStorage:
    FILE_NAME = "tasks.json"
    
    @staticmethod
    def save(tasks):
        with open(JSONStorage.FILE_NAME, "w") as file:
            json.dump([task.to_dict() for task in tasks], file)
    
    @staticmethod
    def load():
        if not os.path.exists(JSONStorage.FILE_NAME):
            return []
        with open(JSONStorage.FILE_NAME, "r") as file:
            return [Task.from_dict(data) for data in json.load(file)]

class CSVStorage:
    FILE_NAME = "tasks.csv"
    
    @staticmethod
    def save(tasks):
        with open(CSVStorage.FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())
    
    @staticmethod
    def load():
        if not os.path.exists(CSVStorage.FILE_NAME):
            return []
        with open(CSVStorage.FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            return [Task.from_dict(row) for row in reader]

if __name__ == "__main__":
    storage_option = input("Choose storage format (json/csv): ").strip().lower()
    storage = JSONStorage() if storage_option == "json" else CSVStorage()
    task_manager = TaskManager(storage)
    
    while True:
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.update_task()
        elif choice == "4":
            task_manager.delete_task()
        elif choice == "5":
            task_manager.filter_tasks()
        elif choice == "6":
            task_manager.save_tasks()
        elif choice == "7":
            task_manager.load_tasks()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
