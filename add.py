"""
This is Script is made to add items and update their prices 
Made by: Dominic Francis
Make Date: 5th August 2022
"""

#FEATURES..
#has to be able to open and read json file
#has to be able to prompt user for data to add or correct
#has to be able to write back to the file

#MODULES...
#json

#### LET's BEGIN #####
#import module
import json


######has to be able to open and read json file #####
with open("resource.json") as f:
    h = json.loads(f.read())
print(h)


#has to be able to prompt user for data to add or correct
#has to be able to write back to the file
