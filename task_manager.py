#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
while True:
    username = input('Enter a Username: ')
    password = input('Enter a password: ')
    text = []
    filename = open('user.txt','r')
    text = filename.readlines()
    user,pas = False,False
    for i in range(len(text)):
        text1 = text[i].strip('\n').split(', ')
        u_name = text1[0]
        pwd = text1[1]
        #print(u_name,pwd)
        if username == u_name:
            user = True
        
        if password == pwd:
            pas = True
        
    if user == True and pas == True:
        print('You are successfully login')
        break
    elif user == True and pas == False:
        print('Incorrect password')
        print('Try again')
    elif user == False and pas == True:
        print('Incorrect usename')
        print('Try again')
    else:
        print('Incorrect usename and password')
        print('Try again')

filename.close()

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r': #and username.lower == 'admin'
        line = []
        username = input('Enter a Username: ')
        while True:
            password = input('Enter a password: ')
            confirm_pass = input('Confirm a password: ')
            if password == confirm_pass:
                file = open('user.txt','a+')
                file.writelines('\n'+username+', '+password)
                line.append(username+', '+password)
                break
            else:
                print('Password Mismatch!')
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

    elif menu == 'a':
        print('''Add the username of the person whom the task is assigned to,
        A title of a task,
        A description of the task and
        The due date of the task''')
        u_name = input('Enter a name whom the task is assigned to:  ')
        task = input('A title of a task:  ')
        detail_task = input('A description of the task:  ')
        due_date = input('The due date of the task: ')
        current_date = datetime.datetime.today()
        filetask = open('tasks.txt','a+')
        filetask.writelines(u_name+', '+ task+', '+ detail_task+', '+ str(current_date)+', '+ str(due_date)+', '+ 'NO'+'\n')
        filetask.close()
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

    elif menu == 'va':
        filetask = open('tasks.txt','r+')
        str_line = []
        print('=========================================================')
        for task in filetask.readlines():
            str_line = task.strip('\n').split(',')
            print('Task:             ', str_line[1])
            print('Assigned to:       ', str_line[0])
            print('Date assigned:    ', str_line[3])
            print('Due date:         ', str_line[4])
            print('Task complete?:   ', str_line[5])
            print('Task description: ', str_line[2])
            print('=========================================================')
           
        filetask.close()
        
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        filetask = open('tasks.txt','r+')
        str_line = []
        print('=========================================================')
        for task in filetask.readlines():
            str_line = task.strip('\n').split(',')
            if username == str_line[0]:
                print('Task:             ', str_line[1])
                print('Assigned to:       ', str_line[0])
                print('Date assigned:    ', str_line[3])
                print('Due date:         ', str_line[4])
                print('Task complete?:   ', str_line[5])
                print('Task description: ', str_line[2])
                print('=========================================================')
           
        filetask.close()
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
file.close()       