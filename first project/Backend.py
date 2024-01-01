from functions import add,reading,writing
import time
k=time.strftime("%c")
print(k)
while True:
    

    
    user_action=input("ENTER TASK ADD,SHOW,EDIT OR COMPLETE OR CLICK EXIT TO LEAVE:--\n")
    user_action.lower()
    user_action=user_action.strip()
    

    if user_action.startswith("add") and len(user_action)>3:
        variable=user_action[4:]
        variable=variable+"\n"
        k1=add(variable)
        writing(k1)


    elif user_action.startswith("show"):
            k=reading()
            
            for i,j in enumerate(k):
                j=j.strip("\n")
                row=f"{i+1}){j}"
                print(row)
                

    elif user_action.startswith("complete"):
            try:
                location=int(user_action[9:])
                ko=reading()
                ko.pop(location-1)
                print(f"{location}th element is deleted")
                writing(ko)

            except IndexError:
                 print("Incorrect index")
            except ValueError:
                 print("Incorrect statement")
                 

    elif user_action.startswith("edit"):
        try:
            place=int(user_action[5:])
            place=place-1
            value=input("enter the value>>")
            k=reading()
            k[place]=value+"\n"
            
            writing(k)
        except ValueError:
                print("COMMAND INVALID!!")
               
            


    elif user_action=="exit":
            break
    
    else:
        print("command is not valid")
print("Have a Nice Day!")
