import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a todo")
input_box = fsg.InputText(tooltip="Enter todo", key='todos')
add_button = fsg.Button("Add")
list_box = fsg.Listbox(values=functions.get_todos(), key='todoslist',
                       enable_events=True, size=[47, 10])
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")

window = fsg.Window('My Todo App',
                    layout=[[label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button, exit_button]],
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
        case 'Complete':
            todo_to_complete = values['todoslist'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todoslist'].update(values=todos)
            window['todos'].update(value='')
        case 'todoslist':
            window['todos'].update(value=values['todoslist'][0])
        case 'Exit':
            quit()
        case fsg.WIN_CLOSED:
            break



window.close()

