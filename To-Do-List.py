print("------To Do List Manager------")
todo_list = []

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    user_choice = input("Enter your choice (1-4): ")

    if user_choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added successfully.")

    elif user_choice == "2":
        if not todo_list:
            print("Your To-Do list is empty.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")

    elif user_choice == "3":
        if not todo_list:
            print("No tasks to mark as completed.")
        else:
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
            try:
                user_remove = int(input("Enter the task number to mark as completed: "))
                if 1 <= user_remove <= len(todo_list):  #this check if the input number is within valid range of the list(from 1 to the number of tasks)
                    removed_task = todo_list.pop(user_remove - 1)
                    print(f"Task '{removed_task}' marked as completed and removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif user_choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")