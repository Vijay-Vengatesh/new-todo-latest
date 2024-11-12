import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a todo")
input_box = fsg.InputText(tooltip="Enter todo", key='todos')
add_button = fsg.Button("Add")
list_box = fsg.Listbox(values=functions.get_todos(), key='todoslist',
                       enable_events=True, size=[47, 10])
edit_button = fsg.Button("Edit")

window = fsg.Window('My Todo App',
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
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
            window['todoslist'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todoslist'][0]
            ntodos = values['todos'] + '\n'

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos.__setitem__(index, ntodos)
            functions.write_todos(todos)
            window['todoslist'].update(values=todos)
        case 'todoslist':
            window['todos'].update(value=values['todoslist'][0])
        case fsg.WIN_CLOSED:
            break



window.close()

