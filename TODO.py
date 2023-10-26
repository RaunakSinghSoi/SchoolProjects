# To-Do List Application

# Function to add a task to the to-do list
def add_task(task_list, task):
    task_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to view the to-do list
def view_tasks(task_list):
    if not task_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")

# Function to mark a task as complete
def mark_task_complete(task_list, task_index):
    if 1 <= task_index <= len(task_list):
        print(f"Task '{task_list[task_index - 1]}' marked as complete.")
        del task_list[task_index - 1]
    else:
        print("Invalid task index.")

# Function to remove a task from the to-do list
def remove_task(task_list, task_index):
    if 1 <= task_index <= len(task_list):
        print(f"Task '{task_list[task_index - 1]}' removed from the to-do list.")
        del task_list[task_index - 1]
    else:
        print("Invalid task index.")

# Function to save the to-do list to a text file
def save_to_file(task_list, filename):
    with open(filename, 'w') as file:
        file.write("\n".join(task_list))
    print(f"To-Do list saved to '{filename}'.")

# Function to load the to-do list from a text file
def load_from_file(filename):
    try:
        with open(filename, 'r') as file:
            task_list = file.read().splitlines()
        print(f"To-Do list loaded from '{filename}'.")
        return task_list
    except FileNotFoundError:
        print("File not found. Starting with an empty to-do list.")
        return []

if __name__ == "__main__":
    task_list = load_from_file("todolist.txt")

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Save To-Do List")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task_list, task)
        elif choice == "2":
            view_tasks(task_list)
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as complete: "))
            mark_task_complete(task_list, task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to remove: "))
            remove_task(task_list, task_index)
        elif choice == "5":
            save_to_file(task_list, "todolist.txt")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please select a valid option.")
