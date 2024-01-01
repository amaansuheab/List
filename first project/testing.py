import PySimpleGUI as sg

layout = [
    [sg.Text("Enter your name:")],
    [sg.InputText(tooltip="Why are you hovering cursor?", key="name")],
    [sg.Button("Submit")]
]
k=[1,2,3]
list=sg.Listbox(values=k,key="List",enable_events=True,size=[15,10])
key=sg.InputText(key="nana")
window = sg.Window("Name Input", layout=[[key],[list]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == sg.WINDOW_CLOSED:
        break
    
    elif event=="nana":
        sg.popup("yo")
    elif event == "List":
        print(event)
        print(values)
        sg.popup(values["List"])
    elif event == "Submit":
        input_value = values["name"]
        sg.popup(f"Hello, {input_value}!")

window.close()
