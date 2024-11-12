import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a todo")
input_box = fsg.InputText(tooltip="Enter todo", key='todos')
add_button = fsg.Button("Add")

window = fsg.Window('My Todo App',
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 20))

while True:
    events, values = window.read()
    print(events)
    print(values)
    match events:
        case 'Add':
            todos = functions.get_todos()
            new_todos = values['todos'] + '\n'
            todos.append(new_todos)
            functions.write_todos(todos_arg=todos)
        case fsg.WIN_CLOSED:
            break



window.close()

