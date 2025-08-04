TODO_file="todo.txt"
def load_tasks():
    try:
        with open(TODO_file,"r") as f:
            return [line.strip() for line in f.readlines()]
    except:
        return []
def save_tasks(tasks):
    with open(TODO_file,"w") as f:
        for task in tasks:
            f.write(task + "\n")
def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
        return
    print("\n ----Your To-Do List----")
    for i,task in enumerate(tasks):
        print(f"{i+1}.{task}")
    print("--------------------\n")
def add_task(tasks):
    new_task= input("Enter the new task: ")
    if new_task:
        tasks.append(new_task)
        print(f"'{new_task}' has been ended")
    else:
        print("A task cannot be empty.")
def remove_tasks(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_number = int(input("Enter the number of the task to remove: "))
        if 1<=task_number <=len(tasks):
            removed_tasks= tasks.pop(task_number -1)
            print(f"'{removed_tasks}' has been removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
        
def main():
    """
    The main function that handels the command -line Interface.
    """
    tasks= load_tasks()
    
    while True:
        print("\n----To-Do App Menu----")
        print("1.View the Tasks")
        print("2.Add a new Task")
        print("3.Remove a Task")
        print("4.Quit and save")
        
        choice= input("Enter your choice (1-4): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice =='3':
            remove_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Your tasks have been saved.Bye!")
            break
        else:
            print("Invalid choice. Please a valid choice")

if __name__ == "__main__":
    main()
    
