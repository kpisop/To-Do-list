import datetime

file = open("todo.txt", "r+")
tasks = [task.strip() for task in file.readlines()]
tasksNo = len(tasks)
print("Welcome to the To-Do List App! \nuse /help for seeing commands\n")
print("Todays Tasks: \n")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")
user_input = input("")
if user_input == "/add":
    task = input("Enter the task you want to add: ")
    now = datetime.datetime.now()
    task_with_time = f"{tasksNo + 1}/{task} (added on {now.strftime('%Y-%m-%d %H:%M:%S')})"
    tasks.append(task_with_time)
    file.write(task_with_time + "\n")
    print("Task added successfully!")
elif user_input == "/clear":
    file.seek(0)
    file.truncate()
    tasks = []
    print("All tasks have been cleared!")

print("Todays Tasks: \n")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

file.close()