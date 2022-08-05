'''
basic order system made by Dominic Francis

'''
import time


menu = {"chicken burger": 20, "smoothy": 10, "meat pie": 15}
resources = {"1" : [30, "chicken burger"], "2": [20, "smoothy"], "3": [23, "meat pie"]}
#menu_list = {"1": "chicken burger", "2": "smoothy", "3": "meat pie"} #this was used in older version of this program
pr, sr, fr= [], [], [] #pr = customer choice price, sr = number ordered, fr = choice of food from menu 


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
        #this commented code was used in previous version  
        """
        if a != "":
            ab = resources.get(a)[1]
            pieces(a, ab)
        elif (a == "r"):
            print(menu)
            print(resources)



def pieces(a, ab):
            b = int(input("how many pieces?: "))
            total_price = 0
            if b > resources.get(a)[0]:
                print(f"\nNot Enough {ab.upper()}\n")
            else:
                print(total_price)
                pr.append(menu.get(ab) * b), sr.append(b), fr.append(ab) #this reduces the lines of code needed
                resources[a][0] = (resources.get(a)[0]- b)
                print("do you want to add an order?(y/n): ")
                answer = input()
                if answer == "y":
                    kkkk()
                else:
                    gr = 0
                    sum = 0
                    for i in pr:
                        sum += i
                    for i in sr:
                        gr += i
                    print(f"your order for {fr}, {gr} quantity price is {sum}")




while True:
    print("Welcome to Cloud Chicken Service\nwhat would you like to eat:\n1. chicken burger\n2. smoothy\n3. meat pie")
    
    kkkk()
    print("Thank you for Shopping at Cloud Chicken Service.\nYour satisfaction is our concern.\nSee you Soon.\nProgram finished\n")
    pr, sr, fr= [], [], [] #pr = customer choice price, sr = number ordered, fr = choice of food from menu  #THEIR RESETS
    time.sleep(3)