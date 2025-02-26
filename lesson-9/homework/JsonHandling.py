import json
import csv


def load_tasks(filename):
    with open(filename, 'r') as file:
        tasks = json.load(file)
    return tasks


def display_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Task Name: {task['task']}, Completed Status: {task['completed']}, Priority: {task['priority']}")


def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)


def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task['completed']])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks
    
    return {
        'Total tasks': total_tasks,
        'Completed tasks': completed_tasks,
        'Pending tasks': pending_tasks,
        'Average priority': average_priority
    }


def convert_to_csv(tasks, csv_filename):
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Task', 'Completed', 'Priority'])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])


tasks = load_tasks('tasks.json')
display_tasks(tasks)
stats = calculate_stats(tasks)
print("\nTask Completion Stats:")
for key, value in stats.items():
    print(f"{key}: {value}")


save_tasks(tasks, 'tasks.json')


convert_to_csv(tasks, 'tasks.csv')
print("\nTasks have been converted to tasks.csv")
