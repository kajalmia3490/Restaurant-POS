from menu import menu_lists

total_order = 0

print("----- Welcome to Restaurant -----")
print(menu_lists)
print("--------------------------------------\n")

# add first item
item1 = input("Select the item: ").lower()
qty = int(input("Quantity: "))

if item1 in menu_lists:
    total_order += menu_lists[item1] * qty
    print(f"{item1}: {menu_lists[item1] * qty} is added.")
else:
    print(f"Ordered item {item1} isn't available yet.")

# add more item
add_more = input("Do you want to add more item? (y/n): ").lower()
qty

if add_more == "y":
    while True:
        item2 = input("Add more item (Press 's' for stop to add): ").lower()
        if item2 == 's':
            break
        else:
            qty_for_item2 = int(input("Quantity: "))

        if item2 in menu_lists:
            total_order += menu_lists[item2] * qty_for_item2
            print(f"{item2}: {menu_lists[item2] * qty_for_item2} is added.")
        elif item2 == 's':
            break
        else:
            print(f"{item2} isn't available yet.")
else:
    print("\n-----------------------------------------")

# add vat and service or not
vat_service = input("Do you want to add VAT/Service? (y/n): ")
while True:
    if vat_service == 'n':
        break
    else:
        # service
        service = int(input("Service % : "))
        service_charge = total_order * (service / 100)

        # vat
        vat = int(input("VAT % : "))
        vat_charge = (total_order + service_charge) * (vat / 100)

        # total calculation
        add_vat_service = total_order + service_charge + vat_charge
        overall_total = add_vat_service
        print("-----------------------------")
        
        # show ordered menu lists
        ordered_menu = []
        if item1 in menu_lists or item2 in menu_lists:
            ordered_menu.append(item1)
        if item2 in menu_lists:
            ordered_menu.append(item2)
        print("-------------------------------")
        print(f"\nYour total amount is {add_vat_service} TK. \nThanks for your sweet order!")
        if add_vat_service:
            break


# billing save as text file
with open("bills.txt", "a") as f:
    f.write(
        f"----------------------------\n"
        f"Menu: \n{item1}\n{item2 or 0}\n"
        f"Service Charge {service}% : {service_charge}\n"
        f"VAT {vat}% : {vat_charge}\n"
        f"Total: {overall_total}"
        f"\n----------------------------\n Thank You!"
    )





    
    
