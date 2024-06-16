class TodoList:
    def _init_(self):
        self.tasks = []

    def show_menu(self):
        print("\n1. Show all tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Exit")

    def show_tasks(self):
        print("\nTasks:")
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Not completed"
            print(f"{i}. {task['task']} - {status}")

    def add_task(self):
        task = input("Enter task: ")
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self):
        self.show_tasks()
        task_number = int(input("Enter task number to delete: "))
        try:
            del self.tasks[task_number - 1]
        except IndexError:
            print("Invalid task number")

    def mark_task_as_completed(self):
        self.show_tasks()
        task_number = int(input("Enter task number to mark as completed: "))
        try:
            self.tasks[task_number - 1]["completed"] = True
        except IndexError:
            print("Invalid task number")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter choice: ")
            if choice == "1":
                self.show_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.mark_task_as_completed()
            elif choice == "5":
                break
            else:
                print("Invalid choice")

if _name_ == "_main_":
    todo_list = TodoList()
    todo_list.run()