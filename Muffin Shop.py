#Rami Ghanem, Student number: 101000509

def doughnutShoppe():       #Defin function as doughnutShoppe
    '''Greeting the user and then promting
    them to select a valid option'''
    option=''               #Option is set to string to clocet user input
    strawberry=0            #Initialize this variable and the next three below as zero so if user click checkout it will show zero orders and a total of zero
    chocolate=0
    vanilla=0
    honey=0
    loop = True             #Make variable loop equal to true
    
    while(loop):            #Loop meant for the repeating of the question as long as user does not put valid input 
        print("Hello and welcome to Dino Doughnut Shoppe how can I help you!") #Greets user to the store
        option = raw_input("1.Order\n2.Check out\n3.Startover\n4.Exit\n ")     #Prompts user to slect a valid option
        if(option!='1'and option!='2' and option!='3' and option!='4'):        #Check to see if user has put in valid option, so if he has not put in 1,2,3,or 4
            print("Error:%r is not a valid input.\n" %(option))                #If invalid input tells the user what the error is 

        if(option == '4'):                                                     #If option 4 is slected goes through the opearation
            print("Good bye, and have a good day")                             #String that says good bye to the user
            loop = False                                                       #Breaks the loop and ends the program 
            
        if(option == '1'):                                                     #If option 1 is selected goes through the opeartion
            strawberry,chocolate,vanilla,honey=order()                         #Takes the user to order function and return the users input
            
        if(option=='3'):                                                       #If option 3 is selected goes through the operation
            strawberry=0                                                       #It reset the next four variable to zero so order is cleared
            chocolate=0
            vanilla=0
            honey=0
            
        if(option == '2'):                                                                          #If option 2 is selected goes through the operation
             strawberry,chocolate,vanilla,honey=checkout(strawberry,chocolate,vanilla,honey)        #Take user to the checkout function with the paremters taken from the order function where they confirm order which gives the total, clearing the order and return to the main menu or cancels order and return them to the main menu with thier prevous order  
                                  
                   
def order():            #Defin function as order
    '''Prompts the user to select from a variety of
    option while looking for valid option'''
    strawberry=''       #Define these four variables as string which allows me to use .isdigit()
    chocolate=''
    vanilla=''
    honey=''

    done=False          #Set done to False
    
    while(done==False): #Allow for the option to loop until user decides to return to the main menu
        ask='0'         #set ask to string of zero
        while(ask!='1'and ask!='2' and ask!='3' and ask!='4'and ask!='5'): #Loops for the selection of option if user put invalid input 
            print("What would you like to order?")                         #Greets the user
            ask = raw_input("1.Strawberry Twizzler: $2.00 each\n2.Chocolate-dipped Maple Puff: $3.25 each\n3.Vanilla Chai Strudel: $2.75 each\n4.Honey-Drizzled Lemon Dutchie: $2.50 each\n5.Done\n ") #Prompts the user a valid option from the list of option 
            if(ask!='1'and ask!='2' and ask!='3' and ask!='4'and ask!='5'):#Check to see if user has put in valid option
                print("Error:%r is not a valid input.\n" %(ask))           #If invalid input tells the user what the error is

        if(ask =='1'):                                                                  #Go through operation of option 1
            while(strawberry.isdigit()==False):                                         #Check to see if user input is digit while it is not it loops the question
                strawberry = raw_input("How much do you want(Must be a digit)?\n ")     #prompts the user for ammount wanted

        if(ask =='2'):                                                                  #Go through operation of option 2
            while(chocolate.isdigit()==False):                                          #Check to see if user input is digit while it is not it loops the question
                chocolate = raw_input("How much do you want(Must be a digit)?\n ")      #prompts the user for ammount wanted
            
        if(ask =='3'):                                                                  #Go through operation of option 3
            while(vanilla.isdigit()==False):                                            #Check to see if user input is digit while it is not it loops the question
                vanilla = raw_input("How much do you want(Must be a digit)?\n ")        #prompts the user for ammount wanted

        if(ask =='4'):                                                                  #Go through operation of option 4
            while(honey.isdigit()==False):                                              #Check to see if user input is digit while it is not it loops the question
                honey = raw_input("How much do you want(Must be a digit)?\n ")          #prompts the user for ammount wanted
        
        if(ask=='5'):                                                                   #Go through operation of option 5
            if(strawberry==''): #So if the user does not select the option changes the string to zero
                strawberry=0    #It sets the variable to zero
            if(chocolate==''):  #So if the user does not select the option changes the string to zero
                chocolate=0     #It sets the variable to zero
            if(vanilla==''):    #So if the user does not select the option changes the string to zero
                vanilla=0       #It sets the variable to zero
            if(honey==''):      #So if the user does not select the option changes the string to zero
                honey=0         #It sets the variable to zero
            done=True                                                                   #Done becomes equal to true breaking the loop
            return strawberry,chocolate,vanilla,honey                                   #Return info to the doughnutShoppe() function


def checkout(strawberry,chocolate,vanilla,honey): #Defin function checkout which use parameters 
    ''' Takes in paramters and gives the user total order of product then prompting to confirm
    for the total cost of products or cancel and return to main menu'''
    strawberry=int(strawberry) #Taking the paramter I convert them all int so they can be used for calaculation as seen in the four variables
    chocolate=int(chocolate)
    vanilla=int(vanilla)
    honey=int(honey)
    print("Your order:")                                                        #Greets the user
    print("You have %d orders of Strawberry Twizzler." %(strawberry))           #Tells the user the amount ordered 
    print("You have %d orders of Chocolate-dipped Maple Puff." %(chocolate))    #Tells the user the amount ordered 
    print("You have %d orders of Vanilla Chai Strudel." %(vanilla))             #Tells the user the amount ordered 
    print("You have %d orders of Honey-Drizzled Lemon Dutchie." %(honey))       #Tells the user the amount ordered 

    option2=''        #set option2 to string to get user input
    while(True):      #Allow the question to be looped
        print("Hello would you like to confirm or cancel your order?")     #Greet the user
        option2 = raw_input("1.Confrim\n2.cancel\n")                       #prompt the user with an option
        if(option2!='1' and option2!='2'):                                 #Checks to see if user has put invalide input
            print("Error:%r is not a valid input.\n" %(option2))           #If invalid input tells the user what the error is

        if(option2=='2'):                                   #if option is equal 2 run operation
            return(strawberry,chocolate,vanilla,honey)      #return the user to the main menu with their previse input
        
        if(option2=='1'):                                                           #if option is equal 1 run operation
            total=(strawberry*2.00)+(chocolate*3.25)+(vanilla*2.75)+(honey*2.50)    #Caculates total cost with parameters given
            total=float(total)                                  #convert the variable to float as to give decimal place to the number
            print("Your total come to: $%.2f" %(total))         #gives the user the total cost of all product he has ordered
            print("Thanks for coming and have a good day.\n")     #Tells the user goodbye
            return(0,0,0,0)                                     #return to the main menu while reseting the input for the next user 
            

#Test 1
#>>> doughnutShoppe()
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# g
#Error:'g' is not a valid input.

#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 1
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# hi
#Error:'hi' is not a valid input.

#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 1
#How much do you want(Must be a digit)?
# 1
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 2
#How much do you want(Must be a digit)?
# 0
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 3
#How much do you want(Must be a digit)?
# -7
#How much do you want(Must be a digit)?
# 5
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 9
#Error:'9' is not a valid input.

#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 4
#How much do you want(Must be a digit)?
# 1
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 5
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 2
#Your order:
#You have 1 orders of Strawberry Twizzler.
#You have 0 orders of Chocolate-dipped Maple Puff.
#You have 5 orders of Vanilla Chai Strudel.
#You have 1 orders of Honey-Drizzled Lemon Dutchie.
#Hello would you like to confirm or cancel your order?
#1.Confrim
#2.cancel
#2
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 1
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 3
#How much do you want(Must be a digit)?
# 1
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 4
#How much do you want(Must be a digit)?
# 2
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 5
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 3
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 1
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 2
#How much do you want(Must be a digit)?
# 2
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 4
#How much do you want(Must be a digit)?
# 3
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 5
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 2
#Your order:
#You have 0 orders of Strawberry Twizzler.
#You have 2 orders of Chocolate-dipped Maple Puff.
#You have 0 orders of Vanilla Chai Strudel.
#You have 3 orders of Honey-Drizzled Lemon Dutchie.
#Hello would you like to confirm or cancel your order?
#1.Confrim
#2.cancel
#1
#Your total come to: $14.00
#Thanks for coming and have a good day.

#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 2
#Your order:
#You have 0 orders of Strawberry Twizzler.
#You have 0 orders of Chocolate-dipped Maple Puff.
#You have 0 orders of Vanilla Chai Strudel.
#You have 0 orders of Honey-Drizzled Lemon Dutchie.
#Hello would you like to confirm or cancel your order?
#1.Confrim
#2.cancel
#1
#Your total come to: $0.00
#Thanks for coming and have a good day.

#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 4
#Good bye, and have a good day






#Test 2
#>>> doughnutShoppe()
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# what
#Error:'what' is not a valid input.

#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 1
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# help
#Error:'help' is not a valid input.

#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 1
#How much do you want(Must be a digit)?
# 6
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 2
#How much do you want(Must be a digit)?
# 0
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 3
#How much do you want(Must be a digit)?
# -25
#How much do you want(Must be a digit)?
# 1
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 9
#Error:'9' is not a valid input.

#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 4
#How much do you want(Must be a digit)?
# 3
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 5
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 2
#Your order:
#You have 6 orders of Strawberry Twizzler.
#You have 0 orders of Chocolate-dipped Maple Puff.
#You have 1 orders of Vanilla Chai Strudel.
#You have 3 orders of Honey-Drizzled Lemon Dutchie.
#Hello would you like to confirm or cancel your order?
#1.Confrim
#2.cancel
#2
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 1
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 3
#How much do you want(Must be a digit)?
# 2
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 4
#How much do you want(Must be a digit)?
# 3
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 5
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 3
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 1
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 2
#How much do you want(Must be a digit)?
# 2
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 4
#How much do you want(Must be a digit)?
# 7
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 5
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 2
#Your order:
#You have 0 orders of Strawberry Twizzler.
#You have 2 orders of Chocolate-dipped Maple Puff.
#You have 0 orders of Vanilla Chai Strudel.
#You have 7 orders of Honey-Drizzled Lemon Dutchie.
#Hello would you like to confirm or cancel your order?
#1.Confrim
#2.cancel
#1
#Your total come to: $24.00
#Thanks for coming and have a good day.

#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 2
#Your order:
#You have 0 orders of Strawberry Twizzler.
#You have 0 orders of Chocolate-dipped Maple Puff.
#You have 0 orders of Vanilla Chai Strudel.
#You have 0 orders of Honey-Drizzled Lemon Dutchie.
#Hello would you like to confirm or cancel your order?
#1.Confrim
#2.cancel
#1
#Your total come to: $0.00
#Thanks for coming and have a good day.

#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 4
#Good bye, and have a good day





#Test 3
#>>> doughnutShoppe()
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# This is the right answer 
#Error:'This is the right answer ' is not a valid input.

#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 1
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# I know it is
#Error:'I know it is' is not a valid input.

#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 1
#How much do you want(Must be a digit)?
# 1
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 2
#How much do you want(Must be a digit)?
# 0
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 3
#How much do you want(Must be a digit)?
# -1
#How much do you want(Must be a digit)?
# 10
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 6
#Error:'6' is not a valid input.

#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 4
#How much do you want(Must be a digit)?
# 5
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 5
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 2
#Your order:
#You have 1 orders of Strawberry Twizzler.
#You have 0 orders of Chocolate-dipped Maple Puff.
#You have 10 orders of Vanilla Chai Strudel.
#You have 5 orders of Honey-Drizzled Lemon Dutchie.
#Hello would you like to confirm or cancel your order?
#1.Confrim
#2.cancel
#2
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 1
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 3
#How much do you want(Must be a digit)?
# 2
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 4
#How much do you want(Must be a digit)?
# 3
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 5
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 3
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 1
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 2
#How much do you want(Must be a digit)?
# 2
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 4
#How much do you want(Must be a digit)?
# 3
#What would you like to order?
#1.Strawberry Twizzler: $2.00 each
#2.Chocolate-dipped Maple Puff: $3.25 each
#3.Vanilla Chai Strudel: $2.75 each
#4.Honey-Drizzled Lemon Dutchie: $2.50 each
#5.Done
# 5
#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 2
#Your order:
#You have 0 orders of Strawberry Twizzler.
#You have 2 orders of Chocolate-dipped Maple Puff.
#You have 0 orders of Vanilla Chai Strudel.
#You have 3 orders of Honey-Drizzled Lemon Dutchie.
#Hello would you like to confirm or cancel your order?
#1.Confrim
#2.cancel
#1
#Your total come to: $14.00
#Thanks for coming and have a good day.

#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 2
#Your order:
#You have 0 orders of Strawberry Twizzler.
#You have 0 orders of Chocolate-dipped Maple Puff.
#You have 0 orders of Vanilla Chai Strudel.
#You have 0 orders of Honey-Drizzled Lemon Dutchie.
#Hello would you like to confirm or cancel your order?
#1.Confrim
#2.cancel
#1
#Your total come to: $0.00
#Thanks for coming and have a good day.

#Hello and welcome to Dino Doughnut Shoppe how can I help you!
#1.Order
#2.Check out
#3.Startover
#4.Exit
# 4
#Good bye, and have a good day
