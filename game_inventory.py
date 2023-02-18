import csv
from io import open

def display_inventory(inventory):
    if isinstance(inventory, dict):
        for item, count in inventory.items():
            print(f"{item}: {count}")
    else: return False

def add_to_inventory(inventory, added_items):
    if isinstance(inventory, dict) and isinstance(added_items, list):
        for item in added_items:
            inventory[item] = inventory.get(item, 0) + 1
    else: return False

def remove_from_inventory(inventory, removed_items):
    if isinstance(inventory, dict) and isinstance(removed_items, list):
        for item in removed_items:
            inventory[item] = inventory.get(item, 0) - 1
            if inventory[item] <= 0: del inventory[item]
    else: return False

def print_table(inventory, order = False):
    print("-----------------")
    print("item name | count")
    print("-----------------")
    if isinstance(inventory, dict):
        if order == "count,asc": sorted_inventory = dict(sorted(inventory.items(), key=lambda x:x[1]))
        elif order == "count,desc": sorted_inventory = dict(sorted(inventory.items(), key=lambda x:x[1], reverse=True))
        else: sorted_inventory = inventory
        for item, count in sorted_inventory.items():
            print(f"{item} | {count}")
    print("-----------------")

def import_inventory(inventory, filename="import_inventory.csv"):
    try:
        with open(filename) as csv_file:
            csv_read = csv.reader(csv_file, delimiter=',')
            for row in csv_read:
                add_to_inventory(inventory, row)
    except:
        print(f"File '<{filename}>' not found!")

    
def export_inventory(inventory, filename="export_inventory.csv"):
    export_list = []
    for item, count in inventory.items():
        i = 0
        while i < count:
            export_list.append(item)
            i += 1
    try:
        with open(filename, "w") as csv_file:
            csv_file.write(','.join(export_list))
    except:
        print(f"File '<{filename}>' not found!")


inventory = {
    "item 3": 2,
    "item 8": 6
}
added_items = ["abcd", "efgh", "item 3", "abcd"]
removed_items = ["item 8", "efgh", "efgh"]

add_to_inventory(inventory, added_items)
remove_from_inventory(inventory, removed_items)

print_table(inventory)
print_table(inventory, "count,asc")
print_table(inventory, "count,desc")

import_inventory(inventory, "import_inventory.csv")

print_table(inventory)

export_inventory(inventory)