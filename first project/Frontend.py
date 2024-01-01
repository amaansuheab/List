import functions
import PySimpleGUI as g
import time


g.theme("Reds")
clock=g.Text("",key="clock")
exit=g.Button('Exit')
complete_button=g.Button("Complete")
edit_button=g.Button("Edit")
label=g.Text("A to do list")
input=g.InputText(tooltip="why are u hovering cursor??",key="todos")
add_button=g.Button("ADD")
list_box=g.Listbox(values=functions.reading(),
                   key="list_box//todos",
                   enable_events=True,
                   size=[50,25])
x=g.Window("Tasks",
           layout=[[clock],[label],[input],[add_button],[[list_box],[edit_button,complete_button,exit]]],
           font=("helvetica",14))
while True:
    a,b=x.read()
    
   
    x["clock"].update(value=time.strftime("%c"))
    
    
    if a=="ADD":
        try:
            
            k=functions.reading()
            k1=b["todos"].strip("\n")
            k1=k1+"\n"
            k.append(k1)
            functions.writing(k)
            x["list_box//todos"].update(values=k)
        except ValueError:
            g.popup("Choose a Correct Value",font=("fantasy",10))

    
    elif a=="Edit":
        try:
            first_value=b["todos"].strip("\n")
            first_value=first_value+"\n"
            second_value=b["list_box//todos"]
            sec_val="".join(second_value)
            reading=functions.reading()
            index1=reading.index(sec_val)
            reading[index1]=first_value
            functions.writing(reading)
            x["list_box//todos"].update(values=reading)

        except ValueError:
            g.popup("Choose a Correct Value",font=("fantasy",10))


    elif a==g.WIN_CLOSED:
        break
    
    elif a=="Exit":
        break

   

    elif a=="list_box//todos":
        j=b["list_box//todos"]
        j="".join(j)
        x["todos"].update(value=j)
        
    elif a=="Complete":

        try:
            
            variable=b["list_box//todos"]
            k2="".join(variable)
            read=functions.reading()
            read.remove(k2)
            functions.writing(read)
            x["list_box//todos"].update(values=read)
        except:
            g.popup("Choose a Correct Value",font=("fantasy",10))

        







x.close()



