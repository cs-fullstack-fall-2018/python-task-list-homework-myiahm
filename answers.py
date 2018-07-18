# Congratulations! You're running [YOUR NAME]'s Task List program.
#
# What would you like to do next?
# 1. List all tasks.
# 2. Add a task to the list.
# 3. Delete a task.
# q. To quit the program
#   function = ["list all task", "Add a task to the list ", "Delete a task" "To quit the program "]
print()

def listAllOptions():
    line1 = (" Congratulations! You're running Myiah's Task List program. \n ")
    line2 = ("1. List all task. \n ")
    line3 = ("2. Add a task to the list. \n ")
    line4 = ("3. Delete a task. \n " )
    line5 = ("q. To quit the program \n ")
    print("{}{}{}{}{}".format(line1, line2, line3, line4, line5))

# def listOptions():

userInput = ["Kenn", "Kevin"]
newTask = ''
userSelection= input("Enter selection: ")

while userSelection != "q":
    listAllOptions()

    if userSelection == ("1"):
        for listOptions in userInput:
            print(listOptions)

    if userSelection == "2":
        newTask= input("enter new task")
        userSelection.append(newTask)

    # userSelection.append(newTask)
    # print(listOptions)
    # if deleteTask in userInput:
    #     userSelection.remove(deleteTask)
    #     print(listOptions)
    userSelection = input("Enter a new selection")
# while userSelection
# filename = (input("User Imput")



