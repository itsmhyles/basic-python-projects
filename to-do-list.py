def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append({"task": task, "completed": False})
            print("Task added successfully!")
        elif choice == '2':
            if tasks:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task["completed"] else " "
                    print(f"{i}. [{status}] {task['task']}")
            else:
                print("No tasks in the list.")
        elif choice == '3':
            if tasks:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task["completed"] else " "
                    print(f"{i}. [{status}] {task['task']}")
                try:
                    task_num = int(input("Enter the task number to mark as complete: ")) - 1
                    if 0 <= task_num < len(tasks):
                        tasks[task_num]["completed"] = True
                        print("Task marked as complete!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks in the list.")
        elif choice == '4':
            print("Thank you for using the To-Do List application!")
            break
        else:
            print("Invalid choice. Please try again.")

todo_list()