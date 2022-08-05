'''
basic order system made by Dominic Francis
Date of Make: Monday, May 23,2022
Date of Edit: Thursday, August 4, 2022

'''
import time
from pandas import pandas as pd 


menu = {"chicken burger": 20, "smoothy": 10, "meat pie": 15}
resources = {"1" : [30, "chicken burger"], "2": [20, "smoothy"], "3": [23, "meat pie"]}
#menu_list = {"1": "chicken burger", "2": "smoothy", "3": "meat pie"} #this was used in older version of this program
pr, sr, fr= [], [], [] #pr = customer choice price, sr = number ordered, fr = choice of food from menu 

def finish(): #had to put this in a function so that i could call it even when the resources is not enough 
    """
    gr = 0
    sum = 0
    """
    gr, sum = 0, 0 #variables to hold the values to be calculated with and written like this reduces number of lines
    """ for i in pr:
        sum += i
    for i in sr:
        gr += i
        #the code here is commented out because it is obselete , still working but old and i have made a new shorter way below """
    for i in range(len(pr)):
        sum += pr[i]
        gr += sr[i]
    print(f"your order for {fr}, {gr} quantity price is {sum}")
    #print(f"\n pr : {pr}, sr : {sr}, length of pr : {len(pr)}, length of sr : {len(sr)}") 
    #i used the above code to define the new for loop to get add the values to sum and gr
    #in a simulation pr is the list of the customer order prices and sr gives the quantity ordered each time
    #one notable thing is that the length of the items in the individual list is same, hence we can use just on of their length

def kkkk():
        a = input("what's your order: ")
        """ if (a == "chicken burger") or (a == "1"):
            if a == "1":
                ab = resources.get(a)[1]
            pieces(a, ab)
        elif (a == "smoothy") or (a == "2"):
            if a == "2":
                ab = resources.get(a)[1]
            pieces(a, ab)
        elif (a == "meat pie") or (a == "3"):
            if a == "3":
                ab = resources.get(a)[1]
            pieces(a, ab)
        elif (a == "r"):
            print(menu)
            print(resources) 
        #this commented code was used in previous version  still working but old, i have made a more vital one below
        """
        #if a != "": #this is an old if condition that allowed any string rather than only key values in the dict keys
        if a in resources.keys(): #this is a more valid condition that also validates the availbility of a in the dict keys
            ab = resources.get(a)[1]
            pieces(a, ab)
        elif (a == "r"): #this prints out the resource in table format
            new = []
            for idx, i in enumerate(range(len(menu)), start=1):
                new.append({"index": idx, "Name": resources[f'{i+1}'][1], "Price": menu.get(resources.get(f'{i+1}')[1]), "NO. Available": resources[f'{i+1}'][0]})
            print(pd.DataFrame(new))
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