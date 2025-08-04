# Task-2
To-Do List app

This program works by loading a list of tasks from a file, presenting a menu to the user, and then performing actions on that list (adding, removing, viewing). When the user is done, the updated list is saved back to the file.

f.write(task + "\n"): It iterates through the list of tasks and writes each one to the file. We add "\n" (a newline character) at the end of each task.
view_tasks(tasks) :
What it does: Prints the list of tasks to the console in a user friendly format.

try-except ValueError: This is another form of error handling. If the user enters text instead of a number (e.g., "hello"), int() will raise a ValueError, and the program will print a friendly error message instead of crashing.

task_number = int(input(...)): To convert the user's input string to an integer.

if 1 <= task_number <= len(tasks):: This is a validation check to make sure the number the user entered is within the valid range of tasks.

tasks.pop(task_number - 1): The pop() method removes an item from a list at a specific index. And subtract 1 from task_number because the user sees a 1-based list, but Python's lists are 0-based.

tasks = load_tasks(): The first thing the program does is load any existing tasks from the file.

while True:: This creates an infinite loop, keeps the program running until the user decides to quit.

input(....) and if/elif/else: This block handles the menu logic. It gets the user's choice and calls the correct function (view_tasks, add_task, etc.) based on that choice.

save_tasks(tasks): The tasks are only saved to the file when the user chooses to "Quit." 
