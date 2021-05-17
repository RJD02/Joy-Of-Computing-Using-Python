import os


def getCount():
    count = 0
    if os.path.getsize('todo.txt') == 0:
        return 0
    with open('todo.txt') as file:
        line = file.readline()
        while line:
            count += 1
            line = file.readline()
    return count


def showTasks():
    if os.path.getsize('todo.txt') == 0:
        print('No tasks left, enjoy the day or add new ones')
        return 0
    with open('todo.txt', 'r') as file:
        line = file.readline()
        while line:
            print(line)
            line = file.readline()
    return 1


def writeToHistory(completed_task):
    with open('todo_history.txt', 'a') as hist:
        hist.write(completed_task[3:])
    return


def deleteTask():
    if(not showTasks()):
        print('Nothing to be deleted')
        return
    task_number = int(
        input('Enter the number of the task which you want to delete: '))
    if task_number > getCount() + 1:
        print('Invalid task number')
        return
    with open('todo.txt', 'r') as file:
        lines = file.readlines()
    with open('todo.txt', 'w') as file:
        count = 0
        for line in lines:
            count += 1
            if count < task_number:
                file.write(line)
            elif count > task_number:
                to_write = str(count - 1) + '. ' + line[3:]
                file.write(to_write)
        showTasks()
        return


def markComplete():
    if(not showTasks()):
        print('Nothing to be marked as complete')
        return
    task_number = int(input('Enter the number of the task which you have completed: '))
    if task_number > getCount() + 1:
        print('Invalid task number')
        return
    with open('todo.txt', 'r') as file:
        lines = file.readlines()
    with open('todo.txt', 'w') as file:
        count = 0
        for line in lines:
            count += 1
            if count < task_number:
                #  to_write = str(count) + '. ' + line[3:]
                file.write(line)
            elif count > task_number:
                to_write = str(count - 1) + '. ' + line[3:]
                file.write(to_write)
            elif count == task_number:
                writeToHistory(line)
    showTasks()
    return

def addTask():
    task = input('Enter the task to add: ')
    with open('todo.txt', 'a') as file:
        if file:
            print('Opened successfully')
            print()
        else:
            print('Encountered a problem while opening the history file')
            print()
            return
        count = getCount()
        to_write = str(count + 1) + '. ' + task + '\n'
        file.write(to_write)
    return

def showHistory():
    with open('todo_history.txt', 'r') as hist:
        if hist:
            print('Opened successfully')
            print()
        else:
            print('Encountered a problem while opening the history file')
            print()
            return
        line = hist.readline()
        while line:
            print(line, end = "")
            line = hist.readline()
    return

def menu():
    choice = -1
    while choice != 6:
        print('Hi there, what do you want to do this time?')
        print('Please go through the following options: ')
        print('1. Add a task to todo list')
        print('2. Mark a task as complete')
        print('3. Delete a task(I suggest you to complete it)')
        print('4. Show the existing todo list')
        print('5. See the history')
        print('6. Exit')
        choice = int(input('Enter your choice here: '))
        if choice == 1:
            addTask()
        elif choice == 2:
            markComplete()
        elif choice == 3:
            deleteTask()
        elif choice == 4:
            showTasks()
        elif choice == 5:
            showHistory()
        else:
            print('Invalid choice')
        print(end='\n')
    return

menu()
