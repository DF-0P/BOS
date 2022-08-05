'''
basic order system made by Dominic Francis
Date of Make: Monday, May 23,2022
Date of Edit: Thursday, August 4, 2022
Facebook : https://www.facebook.com/D.F.0P.1694
'''
import time

menu = {"chicken burger": 20, "smoothy": 10, "meat pie": 15}
resources = {"1" : [30, "chicken burger"], "2": [20, "smoothy"], "3": [23, "meat pie"]}
pr, sr, fr= [], [], []

def finish():
    gr, sum = 0, 0 
    for i in range(len(pr)):
        sum += pr[i]
        gr += sr[i]
    print(f"your order for {fr}, {gr} quantity price is {sum}")
    
def kkkk():
        a = input("what's your order: ")
        if a in resources.keys():
            ab = resources.get(a)[1]
            pieces(a, ab)
        elif (a == "r"):
            print(menu)
            print(resources)
            print("")
        else: #else statement to grab the unknown value gotten
            #pass #used this to start afresh the program initially till i made the line below
            #finish() #used this to print the finish product of their order incase they intended terminating the program , but took it out to make the line below
            print("Please choose the number of the menu item\n")
            kkkk()
            

def pieces(a, ab):
            b = input("how many pieces?: ")
            try: #try state to run
                assert b in str(list(range(100))) #this is to ensure that it's a number thats given and not a letter or character
                total_price = 0
                b = int(b)
                if b > resources.get(a)[0]:
                    print(f"\nNot Enough {ab.upper()}\n")
                    finish()
                else:
                    print(total_price)
                    pr.append(menu.get(ab) * b), sr.append(b), fr.append(ab) #this reduces the lines of code needed
                    resources[a][0] = (resources.get(a)[0]- b) #this appends the new value for the amount of the particular order made
                    answer = input("do you want to add an order?(y/n): ") #question to run to ask whether the want it to run again or not
                    kkkk() if answer == "y" else finish() #this is a tenary statement to run depending on the answer
            except: #except statement to catch the assertion error
                print("Input is not a valid Number.\nTry again.\n")
                pieces(a, ab)

while True:
    print("Welcome to Cloud Chicken Service\nwhat would you like to eat:\n1. chicken burger $20\n2. smoothy $10\n3. meat pie $15")
    kkkk()
    print("Thank you for Shopping at Cloud Chicken Service.\nYour satisfaction is our concern.\nSee you Soon.\nProgram finished\n")
    pr, sr, fr= [], [], [] #pr = customer choice price, sr = number ordered, fr = choice of food from menu  #THEIR RESETS
    time.sleep(3)
