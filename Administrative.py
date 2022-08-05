"""
This is Script is made to add items and update their prices 
Made by: Dominic Francis
Make Date: 5th August 2022
"""
Author = "Made by: Dominic Francis\nMake Date: 5th August 2022\nPlease Give me Credits,it took a while to get this done"
#FEATURES..
#has to be able to open and read json file
#has to be able to prompt user for data to add or correct
#has to be able to search the file for the data
#has to be able to write back to the file with the new data
#has the ability to append new food to the data
#has to be able to get the data of a food item
#MAIN

#MODULES...
#json

#### LET's BEGIN #####
#import module
import json

#### Static Data ####

arrangement = ["Name", "Price", "No. Available"] #used for the position to get from the json object
items_name = {} #used to get the index of the item 
def ite():     #function to use for enumerating the idex and name of the nanme of the foods
    for idx, i in enumerate(h["food"]):
        print(idx, i["Name"])
        items_name[str(idx)] = i["Name"]

##### has to be able to open and read json file #####

with open("resource.json") as f:
    h = json.loads(f.read())
#print(h)


#### has to be able to prompt user for data to add or correct ####

def edith():
    print("Welcome to the Edith Zone:")
    correct = input("1. Name\n2. Price\n3. No. Available\nWhat would you like to change: ") #to prompt the user for the value
    ite() #calls the ite function
    food_correct = input("What is the name of the food/item: ") #to use to search for the value in  the json object
    search(food_correct, correct)

##### has to be able to search the file for the data #####

def search(food_correct, correct):
    new_json = []
    for food in h["food"]:
        if items_name.get(food_correct, "nope") == food["Name"]:
            print(f"\nyessss\nOld value : {food[arrangement[int(correct)-1]]}")
            answer = input("What is the value: ")
            food[arrangement[int(correct)-1]] = answer
            new_json.append(food) #appends the new corrected value dictionary to the list
        else:
            new_json.append(food)
    write(new_json)

##### has to be able to write back to the file with the new data #####

def write(new_json):  #function to write to file
    j = {}
    j["food"] = new_json
    with open("resource.json", "w") as f:
        f.write(json.dumps(j, indent=4))
        print("Successfully Updated.")

##### has the ability to append new food to the data #####
def fd():
    class food_add:
        def __init__(self, Name, Price, No_Available):
            self.name = Name
            self.Price = Price
            self.Available = No_Available
            self.index()
        
        def get_index(self):
            return self.index

        def index(self):
            with open("resource.json") as k:
                l = json.loads(k.read())
            #print(l["food"][len(l["food"])-1]["index"])
            self.index = l['food'][len(l['food'])-1]['index']

        def add(self):
            with open("resource.json", "w") as k: #with function toopenthe  json file
                #print(self.get_index()) #this gets the index number of the last element in the json object
                #structure to add
                o ={"index": self.get_index()+1, "Name": self.name, "Price": self.Price, "No. Available": self.Available}
                h["food"].append(o)
                k.write(json.dumps(h, indent=4))
                print("Added Successfully.")
    add = food_add(input("what is the name of the food: "),input("what is the price you are setting: "),input("How many are in stock Currently:")
)
    add.add()

##### has to be able to get the data of a food item #####
def get():
    class get():
        with open("resource.json") as f:
            f = json.loads(f.read())
            f = f["food"]
        ite()
        ans = int(input("Which Do you want to check value of: "))
        def __init__(self,name=f[ans][arrangement[0]], Price=f[ans][arrangement[1]], No_Available=f[ans][arrangement[2]]):
            self.name = name
            self.price = Price
            self.Available = No_Available
        def g(self):
            print("\nName: ",self.name)
            print("Price: ",self.price)
            print("No Available: ",self.Available)
    get = get()
    get.g()




##### MAIN #####
if __name__ == "__main__":
    welcome = input("Welcome to the Administrative Console.\nWhat you can do:\n1. Add a new food item to the resource file.\n2. Get the information about a food item.\n3. Edith specific info about a food item, such as;\nName\nPrice\nAvailability\nWhat do you want to do: ")
    if welcome == "1":
        fd()
        print(f"\n{Author}")
    elif welcome == "2":
        get()
        print(f"\n{Author}")
    elif welcome == "3":
        edith()
        print(f"\n{Author}")
    else:
        print("invalid key pressed")

    
    
