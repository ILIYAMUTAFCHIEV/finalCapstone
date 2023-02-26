

# HyperionDev Final Capstone Project

#### A Python program for a warehouse, to optimise delivery time and for an improved overview of what each stock-taking session entailed.
---------------------------------------------------------------

## A table of contents:

### inventory.py
### inventory.txt

---------------------------------------------------------------
### 'inventory.py' content:

#### class Shoe

- constructor initialise five attributes
    
- three functions return 'cost', 'quantity' and string representation of a class

#### shoe_list[]

- store a list of objects of shoes
    
#### functions

- read_shoes_data()
   - try to read data from file 'inventory.txt' create objects with this data and add the objects into list
   - skip the first info line, return 'item list' print error message if file not exist
   
- capture_shoes(list)
    - function accept 'item list' print example template and ask the user to enter class attributes
    - create new object and add object into list and file 'inventory.txt', display success message
    -create file if it does not exist
    
- view_all(list)
    - function accept list and display all items
    
- re_stock(list)
    - function accepts list and finds the first object with the lowest quantity
    - read data from the file, depending on the user if he wants to restock, update the quantity

- search_shoe(list)
    - function accepts 'item list', asks the user to enter the shoe code 
    - displays the first object with entered code if the code does not exist print an error message
    
- value_per_item(list)
    - function accepts list and display total value for each item

- highest_qty(list)
    - function accepts list and display the first object with the highest quantity

#### main menu
- read data from file depending user choice call relevant function:

    
    
### 'inventory.txt' content:

#### Text file with data
- one line in this file represents data to create one object of shoes


## Clone the repo
git clone https://github.com/ILIYAMUTAFCHIEV/finalCapstone.git


## Usage section

Start the program and folow instruction

[Screenshot Main Menu.pdf](https://github.com/ILIYAMUTAFCHIEV/finalCapstone/files/10834655/Screenshot.Main.Menu.pdf)

## Contact
Iliya Mutafchiev - https://www.linkedin.com/in/iliya-mutafchiev-974471211/

Project Link: https://github.com/ILIYAMUTAFCHIEV/finalCapstone
