import datetime #importing in-built function of python of date and time
todaydate= datetime.date.today()  #today's date
returndate= datetime.timedelta(days= 10) #date after 10 days
days= (todaydate+returndate) #adding both of them

#opening the textfile "Mainfile" to read
file= open("Mainfile.txt","r")
see= file.readlines()     #reading lines of the data of textfile to convert into whole list
list= []    #declaring a new variable list as a empty list
for line in see:     #for loop
    '''converting whole list made my readlines into 3 separate list of
        different book by appending with empty list spliting by ","'''
    list.append(line.replace("\n", " ").split(","))     
'''after for loop the list are individually changed as separate list.
So, i have initialized 3 variable a,b and c to store individual list.'''
a= list[0]
b= list[1]
c= list[2]
file.close()

#this function ask user to enter their choice 1,2,3 or 4 as users need.
def Welcomeback():
    
    #choose variable is initialized to accept the command from the user.
    choose= int(input("Press 1 to display the books available.... \nPress 2 to borrow books....\nPress 3 to return the borrowed books....\nPress 4 to exit.... \n"))
    
    #choose==1, Displays the avaiable book  
    if(choose==1): 
        
        file= open("Mainfile.txt","r")
        lines= file.readlines()
        for line in lines:
            print(line,"\n")
        a= str(input("Press any key for furthur process....\n"))
        Welcomeback()

    #choose==2 calls and print the booksinlibrary function
    if(choose==2):
        print(booksinlibrary())
        
    #chooose==3 calls and print deposit function
    if(choose==3):
        print(deposit())
        
    #choose==4 exits the program with a greet.
    if(choose==4):
        print("Thank you for your visiting. Please, come back later.")
        exit()

'''function option accepts command from user 1 or 2
option==1, calls the function "welcomeback"
option==2 ends the program with a greet'''
def option():
    option= int(input("Press 1 to continue....\nPress 2 to end the program \n"))
    if(option==1):
        Welcomeback()
    elif(option==2):
        print("Thank you for your visiting. Please, come back later.")
        exit()
'''function fine takes days as a parameter
if the time is less than 10 days, the fine is not added
but if the book is returned after 10 days, the fine of $1 is added per day'''
def fine(days):
    if(days>10):
        time= days-10
        print("You have returned the book on "+ str(todaydate)+ " which crosses the deadline date. \n")
        print("You are charged for returning after 10 days."+"\n")
        fine= (time*1)
        print("The total amount to pay for fine is $"+str(fine)+ "\n")
    elif(days<10) and(days>0):
        print("You have returned the book on time.Thank you! \n")
    
#function borrow accepts the information of the user and append to the text file "Borrow".
def Borrow():
    name= str(input("Enter your name: "))
    address=str(input("Enter your address: "))
    contact= str(input("Enter your contact number: "))
    file= open("Borrow.txt","a")
    file.write("Name: "+ str(name)+ "\n")
    file.write("Address: "+ str(address)+ "\n")
    file.write("Contact: "+ str(contact)+ "\n")
    file.write("Borrowed Date: "+ str(todaydate)+ "\n")
    print("Your details have been saved. \n")
    file.close()

    

#function borrowthebook takes book as a parameter and decrease a book after every borrow. 
def borrowthebook(book):
    if(book==1):
        a[2]= str(int(a[2])-1)
        return a[2]

    elif(book==2):
        b[2]= str(int(b[2])-1)
        return b[2]

    elif(book==3):
        c[2]= str(int(c[2])-1)
        return c[2]
    #end of the function


#function writeinfile updates the textfile "Mainfile" after every borrow or return of the book.
def writeinfile():
    file= open("Mainfile.txt","w")
    file.write(str(a[0])+ ",")
    file.write(str(a[1])+ ",")
    file.write(str(a[2])+ ",")
    file.write(str(a[3])+ "\n")
    
    file.write(str(b[0])+ ",")
    file.write(str(b[1])+ ",")
    file.write(str(b[2])+ ",")
    file.write(str(b[3])+ "\n")
    
    file.write(str(c[0])+ ",")
    file.write(str(c[1])+ ",")
    file.write(str(c[2])+ ",")
    file.write(str(c[3])+ "\n")
    file.close()
    #end of the function

#function depositthebook is defined for choosing and  returning books
def depositthebook():
    file= open("Mainfile.txt","r")
    f= file.readlines()
    for l in f:
        print(l)
    #variable book accept the command fromm the user to choose a number as per their line.  
    book= int(input("choose a number as per their line to return the corresponding book.... \n"))
           
    if(book==1):
        if(a[2]<str(30)):
            name= a[0]
            file= open("Return.txt","a")
            file.write("Book returned: "+ str(name)+"\n")
            file.close()
            a[2]= str(int(a[2])+1)
            return a[2]
            
        else:
            print("The stock is full. You can't return the book!""\n")
            p= input("Press any key to continue....\n")
            Welcomeback()
            
    elif(book==2):
        if(str(int(b[2])-1)<b[2]):
            name= b[0]
            file= open("Return.txt","a")
            file.write("Book returned: "+ str(name)+ "\n")
            file.close()
            b[2]= str(int(b[2])+1)
            return b[2]

        else:
            print("The stock is full. You can't return the book!\n")
            p= input("Press any key to continue....\n")
            Welcomeback()
    elif(book==3):
        if(c[2]<str(20)):
            name= c[0]
            file= open("Return.txt","a")
            file.write("Book returned: "+ str(name)+ "\n")
            file.close()
            c[2]= str(int(c[2])+1)
            return c[2]
        
        else:
            print("You haven't borrowed book yet. The stock is full. \n")
            p= input("Press any key to continue....\n")
            Welcomeback()


#function deposit accepts the details from the user to return the book and append at textfile "Return".
def deposit():
    
    depositthebook()
    name= str(input("Please enter your name: "))
    days= int(input("For how many days did you take the book? ""\n"))
    fine(days)
    file= open("Return.txt","a")
    file.write("Name: "+ str(name)+ "\n")
    file.write("Date in book returned: "+ str(todaydate)+ "\n"+"\n")
    file.close()
    writeinfile()
    print("You have returned the book on",str(todaydate),"\n")
    m= str(input("Thank you for returning the book. Press any key to continue.....\n"))
    Welcomeback()




#function booksinlibrary is defined for choosing and  returning books
def booksinlibrary():
    file= open("Mainfile.txt","r")
    data= file.readlines()
    for i in data:
        print(i)
        
    file.close()
    book= int(input("choose a number as per their line to borrow book the corresponding book.... \n"))
    borrowthebook(book)
    writeinfile()
   
    if(book==1):
        Borrow()
        bookborrowed= a[0]
        file= open("Borrow.txt","a")
        file.write("Book borrowed: "+ str(bookborrowed)+ "\n"+ "\n")
        file.close()
        print("You are supposed to return the book on "+ str(days) + "\n")
        print("The total amount for borrowing the book is: " + str(a[3])+ "\n")
        option()

       
    if(book==2):
        Borrow()
        bookborrowed= b[0]
        file= open("Borrow.txt","a")
        file.write("Book borrowed: "+ str(bookborrowed)+ "\n"+ "\n")
        file.close()
        print("You are supposed to return the book on "+ str(days)+ "\n")
        print("The total amount for borrowing the book is: " + str(b[3])+ "\n")
        option()


    if(book==3):
        Borrow()
        bookborrowed= c[0]
        file= open("Borrow.txt","a")
        file.write("Book borrowed: "+ str(bookborrowed)+ "\n"+ "\n")
        file.close()
        print("You are supposed to return the book on "+ str(days)+ "\n")
        print("The total amount is: "+ str(c[3])+ "\n")
        option()
        
rep='y'
while rep=='y':
    #this function ask user to enter their choice 1,2,3 or 4 as users need.
    def Welcome():
        
        print("--------WELCOME TO LIBRARY--------\n")
        print("Enter your choice: \n")

        #choose variable is initialized to accept the command from the user.
        choose= int(input("Press 1 to display the books available.... \nPress 2 to borrow books....\nPress 3 to return the borrowed books....\nPress 4 to exit....\n"))

        #choose==1, Displays the avaiable book
        if(choose==1):
            file= open("Mainfile.txt","r")
            lines= file.readlines()
            for line in lines:
                print(line)
            file.close()
            a= str(input("Press any key for further process....\n"))
            Welcomeback()

        #choose==2 calls and print the booksinlibrary function   
        if(choose==2):
            booksinlibrary()

        #chooose==3 calls and print deposit function
        if(choose==3):
            deposit()
            
        #choose==4 exits the program with a greet.
        if(choose==4):
                print("Thank you for your visiting. Please, come back later.")
                exit()
    Welcome()
    print("The command is invalid!")
    rep=str(input('Press "y" to restart the program or Press any key to exit.'))
