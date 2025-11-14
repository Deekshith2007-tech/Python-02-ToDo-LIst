TASK_FILE="task.txt"
def load_tasks():
    tasks=[]
    try:
        with open(TASK_FILE,'r')as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks

    
def save_tasks(tasks):
    with open(TASK_FILE,'w')as file:
        for task in tasks:
            file.write(task+'/n')

def show_tasks(tasks):
    if not tasks:
        print("Task is not available.")
    else:
        for idx,task in enumerate(tasks,1):
            print(f"{idx}.{task}")
    
def add_task(tasks):
    task=input("Enter the task to add:").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Empty task cannot be added")

    
def remove_task(tasks):
    show_tasks(tasks)
    try:
        num=int(input("Enter the task number to remove:"))
        removed=tasks.pop(num-1)
        save_tasks(tasks)
        print(f"Task '{removed}' removed successfully.")
    except (ValueError,IndexError):
        print("Invalid task number.")

def main():
    tasks=load_tasks()
    while True:
        print("\n---TO-DO LIST MENU---")
        print("1.Show Tasks")
        print("2.Add Task")
        print("3.Remove Task")
        print("4.Exit")
        choice=input("Enter your choice(1-4):").strip()
        if choice=='1':
            show_tasks(tasks)
        elif choice=='2':
            add_task(tasks)
        elif choice=='3':
            remove_task(tasks)
        elif choice=='4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=='__main__':
    main()      