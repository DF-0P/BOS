'''
basic order system made by Dominic Francis
Date of Make: Monday, May 23,2022
Date of Edit: Thursday, August 4, 2022

'''
#FEATURES...

#MODULES...
#json
#pandas
#time

##### LET'S BEGIN #####
#import Modules
import time
from pandas import pandas as pd 
import json 

##### Data sets #####
menu = {}
resources = {}
pr, sr, fr= [], [], [] 
with open("resource.json") as f:
    h = json.loads(f.read())

def ite():     #function to use for enumerating the idex and name of the nanme of the foods and also for the display menu order
    for idx, i in enumerate(h["food"], start=1):
        print(idx, i["Name"])
        #items_name[str(idx)] = i["Name"] #this is not needed ...its only needed for the administatrtive script

for value in h["food"]: 
    menu[value["Name"]] = int(value["Price"])
    resources[f"{value['index']}"]= [int(value["No. Available"]), value["Name"]]

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
            new = []
            for idx, i in enumerate(range(len(menu)), start=1):
                new.append({"index": idx, "Name": resources[f'{i+1}'][1], "Price": menu.get(resources.get(f'{i+1}')[1]), "NO. Available": resources[f'{i+1}'][0]})
            print(pd.DataFrame(new))
        elif a == "f":
            finish()
        else:
            print("Please choose the number of the menu item\n")
            kkkk()
            
def pieces(a, ab):
            b = input("how many pieces?: ")
            try:
                assert b in str(list(range(100)))
                b = int(b)
                if b > resources.get(a)[0]:
                    print(f"\nNot Enough {ab.upper()}\n")
                    finish()
                else:
                    pr.append(menu.get(ab) * b), sr.append(b), fr.append(ab) 
                    resources[a][0] = (resources.get(a)[0]- b)
                    answer = input("do you want to add an order?(y/n): ")
                    kkkk() if answer == "y" else finish()
            except:
                print("Input is not a valid Number.\nTry again.\n")
                pieces(a, ab)

while True:
    print("Welcome to Cloud Chicken Service\nwhat would you like to eat:")
    ite()
    kkkk()
    print("Thank you for Shopping at Cloud Chicken Service.\nYour satisfaction is our concern.\nSee you Soon.\nProgram finished\n")
    pr, sr, fr= [], [], []
    time.sleep(3)