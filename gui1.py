import FreeSimpleGUI as sg
import functions
import time

sg.theme("Black")

lable = sg.Text("Enter to-do item")
text_box = sg.InputText(tooltip="Enter to-do item", size=46, key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit", size=10)
complete_button = sg.Button("Complete", size=10)
exit_button = sg.Button("Exit")

layout = [[lable],[text_box, add_button],[list_box, edit_button, complete_button],[exit_button]]

window = sg.Window("My TO-DO App", layout, font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event, values)
    
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
            
        case "Exit":
            break
        
        case sg.WIN_CLOSED:
            break
        
window.close()