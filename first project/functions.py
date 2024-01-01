def add(variable):
    r=open("todos.txt","r").readlines()
    r.append(variable)
    return r

def reading(file="todos.txt"):
     r=open(file,"r").readlines()
     return r


def writing(a):
    g=open("todos.txt","w")
    g.writelines(a)

    