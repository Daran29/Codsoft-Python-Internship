tasks=[]

def task_list(tasks):
    for i in tasks: 
        print((tasks.index(i)+1),".",i,)
        
if __name__ == "__main__":
    print("TO DO LIST")
    print("----------------")
    while True:
        print("----------------")
        print("1. LIST TASKS")
        print("2. ADD TASK")
        print("3. DELETE TASK")
        print("4. EXIT")
        print("----------------")
        choice=int(input("YOUR CHOICE?:"))
        
        if(choice==1):
            print("The current tasks are:\n")
            task_list(tasks)
            print("----------------")
            
        elif(choice==2):
            num=int(input('Enter the number of tasks to add: '))
            for i in range(num):
                task=str(input("ENTER A NEW TASK: "))
                tasks.append(task)
            print("New task(s) added.\n")
            task_list(tasks)
            print("----------------")
            
        elif(choice==3):
            remove= int(input("Enter the task number to be removed:"))
            tasks.pop(remove-1)
            print("The Task has been removed\n")
            task_list(tasks)
            print("----------------")
            
        elif(choice==4):
            print("Exiting To Do list Application.....")
            break
        
        else:
            print("Invalid input! Please try again.")