

class ItemToPurchase:
    # Constructor method to initialize its default properties
    def __init__(self, name = "none", description = "none", price = 0, quantity =0):
        self.item_name = name                 #Sting
        self.item_price = price               #float
        self.item_quantity = quantity         #int
        self.item_description = description   #string

    def total_cost(self):
        return self.item_price * self.item_quantity



# Class: ShoppingCart
class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1,2020"):
        self.customer_name = customer_name      #string, like a name tag on the shopping cart
        self.current_date = current_date       # string, the current date on the shopping cart
        self.cart_items = []                   # empty list, empty shopping cart


# methods

    def add_item(self, item):
        self.cart_items.append(item)   # take the item and add it to the shopping cart. Doesn't return anything


    def remove_item(self, item_name):   # the item name that will be input to remove
        for index, item in enumerate(self.cart_items):
            if item.item_name.lower() ==  item_name.lower():
                del self.cart_items[index]
                return
            print("No item founding cart. Nothing was removed")


        def get_cart_items(self):
            return self.cart_items


    def modify_item(self, item_to_modify):
        for item in self.cart_items:
            if item.item_name.lower() == item_to_modify.item_name.lower():
                if item_to_modify.item_price !=0.0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity !=0:
                    item.item_quantity = item_to_modify.item_quantity
                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description
                print(f"{item.item_name} has been updated.")
                return
        print("Item not found in cart. Nothing to modify")


    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)


    def get_cost_of_cart(self):
        return sum(item.total_cost() for item in self.cart_items)


    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        total_items = self.get_num_items_in_cart()
        print(f"Number of Items: {total_items}")
        if total_items == 0:
            print("Your cart is empty")
        else:
            for item in self.cart_items:
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.total_cost()}")
            print(f"Total: ${self.get_cost_of_cart()}")


    def print_description(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions:")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


# ----------------------------------------------------------------------
# Functions: print_Menu
# -----------------------------------------------------------------------

# This function makes the Online shopping cart invoice clear organize and easy to read
def print_Invoice(cart):
    print(f"Customer Cart Name:{cart.customer_name} \t Purchase Date:{cart.current_date}")
    total_quantity = cart.get_num_items_in_cart()
    print("{:>10} {:<10}".format("Total Quantity of Items:", total_quantity))

    print("-" * 85)
    print("{:<10} {:<20} {:<10} {:>15} {:>15}".format("Item", "Description", "Item Quantity", "Cost Per Unit",
                                                          "Total"))
    print("-" * 85)


    grand_total = 0
    for i, item in enumerate(cart.cart_items):
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



# The Print menu function

def print_menu(cart):
    while True:
        print("\n" + "+" + "-" * 30 + "+")
        print("|{:^30}|".format(" MENU "))
        print("+" + "-" * 30 + "+")
        print("| a - Add item to cart         |")
        print("| r - Remove item from cart    |")
        print("| c - Change item quantity     |")
        print("| i - Shows item descriptions |")
        print("| o - Output cart invoice      |")
        print("| q - Quit                     |")
        print("+" + "-" * 30 + "+")

        option = input("Select an option:").lower()

        if option == 'a':
            print("Adding items to your cart...")
            print("Type the word *MENU* to return back to the main menu. \n")

            while True:
                name = input("Item Name: ")
                if name.lower() == "menu":
                    break

                description = input("Enter the item description: ")
                if description.lower() == "menu":
                    break

                try:
                    price_input = input("Enter the item price: ")
                    if price_input.lower() == "menu":
                        break
                    price = float(price_input)

                    quantity_input = input("Enter the quantity: ")
                    if quantity_input.lower() == "menu":
                        break
                    quantity = int(quantity_input)
                except ValueError:
                    print("Error! Please enter valid numeric values for price and quantity.")
                    continue

                item = ItemToPurchase()
                item.item_name = name
                item.item_description = description
                item.item_price = price
                item.item_quantity = quantity
                cart.add_item(item)
                print("Item added to cart.\n")


        elif option == 'r':
            name = input("Enter the item to remove:")
            cart.remove_item(name)

        elif option == 'c':
            name = input("Enter name of item to modify:")
            try:
                new_price = float(input("Enter new price:"))
                new_quantity = int(input("Enter new quantity: "))
            except ValueError:
                print("Error: Invalid input.")
                continue

            item = ItemToPurchase()
            item.item_name = name
            item.item_price = new_price
            item.item_quantity = new_quantity
            cart.modify_item(item)

        elif option == 'i':
            cart.print_description()

        elif option == 'o':
            print_Invoice(cart)

        elif option == 'q':
            print(" Exit application")
            break
        else:
            print("Wrong option. Please choose again.")



# ----------------------------------------------------------------------
# The Main Program
# -----------------------------------------------------------------------

def main():
    # get user information
    customer_name = input("Customer Shopping Cart Name:")
    current_date = input("Enter Today's date:")
    cart = ShoppingCart(customer_name,current_date)

    print("\nA Shopping Cart Has Been Created For:")
    print(f"Customer: {customer_name}\nCurrent Date: {current_date}")

    print_menu(cart)

# Run the program
if __name__ == "__main__":
    main()



