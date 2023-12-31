#create dictionary for storing tasks

tasks = []

#create display menu giving user choice

def display_menu():
    print("===== To-Do List App =====")
    print("1. Create task")
    print("2. Update task status")
    print("3. View tasks")
    print("4. Exit")

#function to create task
    
def create_task():
    description = input("Enter task description: ")
    task = {"description": description, "status": "Not started"}
    tasks.append(task)
    print("Task created successfully!")

#function to update task
    
def update_task_status():
    view_tasks()
    task_index = int(input("Enter the task number to update: ")) - 1

    if 0 <= task_index < len(tasks):
        status = input("Enter task status: ").capitalize()
        tasks[task_index]["status"] = status
        print("Task status updated successfully!")
    else:
        print("Invalid task number.")

#function to view task

def view_tasks():
    print("===== Your Tasks =====")
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['description']} ({task['status']})")

#getting choice from user
            
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        create_task()
    elif choice == "2":
        update_task_status()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Exiting the To-Do List")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
