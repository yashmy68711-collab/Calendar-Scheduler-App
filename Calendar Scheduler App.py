class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task_name = input("Enter task name: ").strip()
        task_date = input("Enter task date (DD-MM-YYYY): ").strip()

        if task_name == "" or task_date == "":
            print("Invalid input")
            return

        task = {
            "name": task_name,
            "date": task_date
        }

        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks scheduled")
            return

        print("\n--- Scheduled Tasks ---")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task['name']} - {task['date']}")

    def delete_task(self):
        self.view_tasks()

        if len(self.tasks) == 0:
            return

        try:
            index = int(input("Enter task number to delete: "))
        except:
            print("Invalid input")
            return

        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"Deleted task: {removed['name']}")
        else:
            print("Invalid task number")


scheduler = Scheduler()

while True:
    print("\n--- Calendar Scheduler App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        scheduler.add_task()

    elif choice == "2":
        scheduler.view_tasks()

    elif choice == "3":
        scheduler.delete_task()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")