import functions
import PySimpleGUI as sg
label=sg.Text("Type in a todo")
input_box=sg.InputText(tooltip="Enter todo",key="todo")
add_button=sg.Button("Add")
edit_button=sg.Button("Edit")
complete_button=sg.Button("Complete")
Exit_button=sg.Button("Exit")
list_box=sg.Listbox(values=functions.get_todos(), key="todos",enable_events=True, size=[45,10])
window=sg.Window("My To-Do App", layout=[[label]
    ,[input_box,add_button]
    ,[list_box,edit_button, complete_button],
                                         [Exit_button]],font=('Helvetica',20))
while True:
    event,values=window.read()
    print(event)
    print(values)
    if event=="Add":
            todos=functions.get_todos()
            new_todo=values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo'].update(value="")
    if event=="Edit":
        todo_to_edit=values["todos"][0]
        new_todo=values["todo"]
        todos=functions.get_todos()
        index=todos.index(todo_to_edit)
        todos[index]=new_todo
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    if event=="todos":
        window['todo'].update(value=values['todos'][0])
    if event=="Complete":
        todos_to_complete=values['todos'][0]
        todos=functions.get_todos()
        todos.remove(todos_to_complete)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value="")
    if event==sg.WIN_CLOSED:
            break
    if event=="Exit":
        break

window.close()