from menu import menu_lists

total_order = 0

print("----- Welcome to Restaurant -----")
print(menu_lists)

# add first item
item1 = input("Select the item: ").lower()
if item1 in menu_lists:
    total_order += menu_lists[item1]
    print(f"{item1}: {menu_lists[item1]} is added.")
else:
    print(f"Ordered item {item1} isn't available yet.")

# add more item
add_more = input("Do you want to add more item? (y/n): ").lower()
if add_more == "y":
    while True:
        item2 = input("Add more item (if press 'c' for no more add): ").lower()
        if item2 in menu_lists:
            total_order += menu_lists[item2]
            print(f"{item2}: {menu_lists[item2]} is added.")
        elif item2 == 'c':
            break
        else:
            print(f"{item2} isn't available yet.")
else:
    print("\n...............................................")

# add vat and service or not
vat_service = input("Do you want to add VAT/Service? (y/n): ")
if vat_service == "y":
    # service
    service = int(input("Service % : "))
    service_charge = total_order * (service / 100)

    # vat
    vat = int(input("VAT % : "))
    vat_charge = (total_order + service_charge) * (vat / 100)

    # total calculation
    add_vat_service = total_order + service_charge + vat_charge
    overall_total = add_vat_service
    print("........................")
    
    # show ordered menu lists
    if item1 in menu_lists or item2 in menu_lists:
        print(f"\nOrdered Items: \n{item1}\n{item2}")
    print("........................")
    print(f"\nYour total amount is {add_vat_service} TK. \nThanks for your sweet order!")
else:
    # service
    service = int(input("Service % : "))
    service_charge = total_order * (service / 100)

    # vat
    vat = int(input("VAT % : "))
    vat_charge = (total_order + service_charge) * (vat / 100)

    # total calculation
    add_vat_service = total_order + service_charge + vat_charge
    print(f"\nYour Total Order Is {add_vat_service} TK. \nThanks for your sweet order!")





    
    
