#========The beginning of the class==========
# Class 'Shoe' constructor initialise five attributes
# Three functions return 'cost', 'quantity and string representation of a class
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
       
    def get_cost(self):
        return float(self.cost)

    def get_quantity(self):
        return float(self.quantity)

    def __str__(self):
        return f'''
        ===========================
        Country: | {self.country}   
        ---------+-----------------
        Code:    | {self.code}     
        ---------+-----------------
        Product: | {self.product}  
        ---------+-----------------
        Cost:    | {self.cost}    
        ---------+-----------------
        Quantity:| {self.quantity}
        ==========================='''

#=============Shoe list===========
# Store a list of objects of shoes.
shoe_list = []

#==========Functions outside the class==============
# Try to read data from file 'inventory.txt' create objects with this data and add the objects into list
# Skip the first info line, return 'item list' print error message if file not exist
def read_shoes_data():
    try:
        item_list = []
        with open("inventory.txt", 'r') as file1:
            for n,line in enumerate(file1):
                if n == 0:
                    continue
                shoe_line = line.strip("\n").split(",")
                shoe = Shoe(shoe_line[0], shoe_line[1], shoe_line[2], shoe_line[3], shoe_line[4])
                item_list.append(shoe)
        return item_list
    except FileNotFoundError:
        print("File inventory.txt not available")

# This function accept 'item list' print example template and ask the user to enter class attributes
# Create new object and add object into list and file 'inventory.txt', display success message
# Create file if it does not exist
def capture_shoes(item_list):

    if len(item_list) > 0:
        for line in item_list:
            print("\n            (EXAMPLE TEMPLATE)")
            print(line)
            break
    else:
        print("Please enter first item in the list in format\n\nCountry\nCode\nProduct\nCost\nQuantity\n")

    country = input("Please enter country: ")
    code = input("Please enter code: ")
    product = input("Please enter product: ")
    cost = input("Please enter cost: ")
    quantity = input("Please enter quantity: ")

    shoe = Shoe(country, code, product, cost, quantity)
    item_list.append(shoe)

    with open("inventory.txt", 'a') as file1:
        file1.writelines(f"\n{country},{code},{product},{cost},{quantity}")
    print("\nSuccessfully add shoe in the shoe list.")
    
# Function accept 'item list' and display all items in a readable format
def view_all(item_list):
    for s in item_list:
        print(s.__str__())
    
# This function accepts 'item list' and finds the first object with the lowest quantity
# Read data from the file, depending on the user if he wants to restock, update the quantity
def re_stock(item_list):
    min_value = float('inf')
    line_num = 0

    for n,item in enumerate(item_list):
        if int(item.quantity) < min_value:
            min_value = int(item.quantity)
            line_num = n

    print("\n            (SHOE TO RESTOCK)")
    print(item_list[line_num].__str__())

    line_num += 1                           # Increase with 1 to add the first line of the file in the count
    quantity_to_add = 50

    with open("inventory.txt", 'r') as file:
        get_all = file.readlines()

    with open("inventory.txt",'w') as file:
        for i,line in enumerate(get_all):           
            if i == line_num:
                new_quantity = input(f"Do you want to add {quantity_to_add} to that quantity(enter: y -> yes, n -> no)\n").lower()
                if new_quantity == 'y':
                    line = line.strip("\n").split(",")
                    line[4] = int(line[4]) + quantity_to_add
                    line[4] = str(line[4])
                    print(f"The new quantity of this shoe is: {line[4]}")
                    line = ','.join(line)
                    file.writelines(f"{line}\n")
                elif new_quantity == 'n':
                    file.writelines(line)
                    continue
                else:
                    file.writelines(line)
                    print("Wrong input")
            else:
              file.writelines(line)
       
# This function accepts 'item list', asks the user to enter the shoe code 
# Displays the first object with entered code if the code does not exist print an error message
def search_shoe(item_list):
    code_list = []

    for shoe in item_list:
        code_list.append(shoe.code)

    shoe_code = input("Please enter shoe code:\n")
    if shoe_code in code_list:
        for item in item_list:
            if item.code == shoe_code:
                print(item.__str__())
    else:
        print("Wrong code!!! Please try again")
    
# This function accepts 'item list' and display total value for each item
def value_per_item(item_list):
    for item in item_list:
        total_item_value = item.get_cost() * item.get_quantity()
        print(f"{item}\nTotal value ot this shoe is: {format(total_item_value, '.2f')}" )
 
# This function accepts 'item list' and display the first object with the highest quantity
def highest_qty(item_list):
    max_value = float('-inf')
    line_num = 0
    for n,item in enumerate(item_list):
        if int(item.quantity) > max_value:
            max_value = int(item.quantity)
            line_num = n

    print("\n       (THE SHOE AS BEING FOR SALE)")
    print(item_list[line_num].__str__())

#==========Main Menu=============
# Read data from file depending user choice call relevant function
while True:
    shoe_list = read_shoes_data()
    main_menu = input('''
Welcome to the Nike warehouses! What would you like to do?
Press:
a -> Add new shoe in stock.
c -> Calculate the total value of each stock item.
s -> Search products by code.
v -> View all the details of the shoes.
l -> Determine the product with the lowest quantity and restock it.
h -> Determine the product with the highest quantity and being for sale.
e -> Exit this program.
''')
    
    if main_menu == 'a':
        capture_shoes(shoe_list)
    elif main_menu == 'c':
        value_per_item(shoe_list)
    elif main_menu == 's':
        search_shoe(shoe_list)
    elif main_menu == 'v':
        view_all(shoe_list)
    elif main_menu == 'l':
        re_stock(shoe_list)
    elif main_menu == 'h':
        highest_qty(shoe_list)
    elif main_menu == 'e':
        print("Good Bye!")
        break
    else:
        print("Wrong input! Please try again")