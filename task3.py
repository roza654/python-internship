def addtk(ts,tk):
    ts.append(tk)
    print(f"task '{tk}' added")
def view(ts):
    if not ts:
        print("no tasks")
    else:
        print("tasks:")
        for i,tk in enumerate(ts):
            print(f"{i+1}.{task}")
def delete_ts(ts):
    view(ts)
    try:
        index=int(input("enter the task to delete"))-1
        del ts[index]
        print("task deleted")
    except(ValueError,IndexError):
        print("invalid input")
ts=[]
while True:
    print("\n To-Do-list")
    print("1. add task")
    print("2.view task")
    print("3.delete task")
    print("4. exist")
    n=int(input("enter no (1-4):"))
    if n==1:
        tk=input("enter the task:")
        addtk(ts,tk)
    elif n==2:
        view(ts)
    elif n==3:
        delete_ts(ts)
    elif n==4:
        print("existing..")
    
    else:
        print("invalid choice")



    
