# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification

# Displays the inventory.
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):

    print("Inventory: ")
    total_item = 0
    for key, value in inventory.items():
        print(str(value) + "   " + str(key))
        total_item += value

    print("Total number of items: " + str(total_item))
    pass

display_inventory(inv)

# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):

    for i in range(len(added_items)):
        added_items = dragon_loot

        inventory.setdefault(added_items[i],0)
        inventory[added_items[i]] = inventory[added_items[i]] + 1

    return inv

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)

display_inventory(inv)

# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order

count_desc = sorted(inv.items(), key=lambda x: x[1])

def print_table(inventory, order=None):

    head = {'count': 'item name'}
    head_set = head.items()
    for row in head_set:
        print("{0:>8} {1:>12}".format(*row))

    print(" --------------------")

    table = sorted(inv.items(), key=lambda x: x[1])
    for row in table:
        print("{1:>8} {0:>12}".format(*row))

    print(" --------------------")

    total_item = 0
    for key, value in inv.items():
        total_item += value
    print(" Total number of items: " + str(total_item))


print_table(inv)

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):

    lista = list(inv)
    import csv
    with open('import_inventory.csv') as csvfile:
        itemreader = csv.reader(csvfile, delimiter=',')
        for row in itemreader:
            print(row)

    pass

import_inventory(inv, filename="import_inventory.csv")
print_table(inv)

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):

    lista = list(inv)       # miert nem mukodik settel?!
    import csv
    with open('import_inventory.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        wr.writerow(lista)
    pass

export_inventory(inv, filename="export_inventory.csv")
