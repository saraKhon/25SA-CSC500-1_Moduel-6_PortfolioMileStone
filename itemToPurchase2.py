
# Mile stone 06

# Step 1 : create the ItemToPurchase class
class ItemToPurchase:
    def __init__(self):
        self.item_name ="none"    #Sting
        self.item_price = 0.0     #float
        self.item_quantity = 0    #int


    def total_cost(self):
        return self.item_price * self.item_quantity


# This function makes the Online shopping cart invoice clear organize and easy to read
def print_Invoice(items):
    print("-" * 85)
    print("{:<10} {:<20} {:<10} {:>15} {:>15}".format("Item", "Description", "Item Quantity", "Cost Per Unit",
                                                          "Total"))
    print("-" * 85)
    grand_total = 0

    for i, item in enumerate(items):
        total = item.total_cost()
        print("{:<10}{:<30}{:<5} {:>12} {:>18}".format(
            f"Item {i + 1}", item.item_name, item.item_quantity,
            f"${item.item_price:,.2f}", f"${total:,.2f}"))

        grand_total += total

    tax = grand_total * 0.10
    final_total = grand_total + tax

    print("-" * 85)
    print("{:>70} ${:<10.2f}".format("Total Price test:", grand_total))
    print("{:>70} ${:<10.2f}".format("Tax (10%): ", tax))
    print("{:>70} ${:<10.2f}".format("Total with Tax: ", final_total))



items = []
item_num = 1

# instructions
print("-" * 85)
print("{:<10}".format("Enter the name of the item to purchase...(Type 'DONE' to Exit "))
print("-" * 85)

while True:
    name = input("Item Name: ")
    if name.lower() == "done":
        break

    try:
        price = float(input("Enter the price:"))
        quantity = int(input("Enter the quantity:"))
    except ValueError:
        print("Error!!! Please enter a numeric value for item price and quantity")
        continue

    item = ItemToPurchase()
    item.item_name = name
    item.item_price = price
    item.item_quantity = quantity

    items.append(item)
    item_num +=1
    print("-" * 85 )


# print the invoice only if there are items
if items:
    print_Invoice(items)
else:
    print("No items found in cart")






