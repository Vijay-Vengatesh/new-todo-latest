
from functions import *
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

while True:
    user_input = input("Type add,show,edit,complete or exit: ").strip()

    if user_input.startswith('add'):
        todo = user_input[4:] + '\n'
        todos = get_todos()

        todos.append(todo)

        write_todos(todos)
    elif user_input.startswith('show'):
        todos = get_todos('todos.txt')
        for index, item in enumerate(todos):
            index = index + 1
            row = f"{index}.{item}"
            newRow = row.replace('\n', '')
            print(newRow)
    elif user_input.startswith('edit'):
        try:
            number = int(user_input[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ") + '\n'
            todos.__setitem__(number, new_todo)

            write_todos(todos)
        except ValueError:
            print("Check your input properly")
            continue
    elif user_input.startswith('complete'):
        try:
            try:
                number = int(user_input[9:])
                number = number - 1
                todos = get_todos()

                todo_to_remove = todos[number].strip('\n')
                todos.pop(number)

                write_todos(todos)

                message = f"the todo --{todo_to_remove}-- is removed"
                print(message)
            except ValueError:
                print("Check your input properly")
                continue
        except IndexError:
            print("Check your input properly")
            continue
    elif user_input.startswith('exit'):
        break
    else:
        print("Command is not valid")


print('Bye')