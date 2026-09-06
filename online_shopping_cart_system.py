

class ItemToPurchase:

    # initialize objects to use
    def __init__(self, name="none", price=0.0, qty=0, description="none"):
        self.item_name = name
        self.item_price = round(price, 2)
        self.item_quantity = qty
        self.item_description = description

    # get cost
    def print_item_cost(self):
        total = round(self.item_price * self.item_quantity, 2)
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")
        return total

    # print description
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:

    # initialize shopping cart
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # add item to cart
    def add_item(self, item):
        self.cart_items.append(item)

    # remove item
    def remove_item(self, name):
        found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == name:
                self.cart_items.pop(i)
                found = True
                break
        if not found:
            print("Your item was not found in cart.")

    # modify item
    def modify_item(self, updated_item):
        found = False
        for item in self.cart_items:
            if item.item_name == updated_item.item_name:
                found = True
                if updated_item.item_description != "none":
                    item.item_description = updated_item.item_description
                if updated_item.item_price != 0.0:
                    item.item_price = updated_item.item_price
                if updated_item.item_quantity != 0:
                    item.item_quantity = updated_item.item_quantity
                break
        if not found:
            print("Your item was not found in cart.")

    # get total number of items in cart
    def get_num_items_in_cart(self):
        count = 0
        for item in self.cart_items:
            count += item.item_quantity
        return count

    # get total cost of cart
    def get_cost_of_cart(self):
        total = 0.0
        for item in self.cart_items:
            total += item.item_price * item.item_quantity
        return total

    # print cart total
    def print_total(self):
        print(f"{self.customer_name}'s shopping cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")

        if len(self.cart_items) == 0:
            print("Your shopping cart is empty")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        print(f"\nTotal: ${self.get_cost_of_cart():.2f}")

    # print item descriptions
    def print_descriptions(self):
        print(f"{self.customer_name}'s shopping cart - {self.current_date}\n")
        print("Item Descriptions")

        if len(self.cart_items) == 0:
            print("Your shopping cart is empty")
        else:
            for item in self.cart_items:
                item.print_item_description()


def print_menu(cart):
    choice = ""

    while choice != "q":
        print("\nMENU")
        print("a: Add item")
        print("r: Remove item")
        print("c: Change item quantity")
        print("i: Output descriptions")
        print("o: Output shopping cart")
        print("q: Quit shopping cart")

        choice = input("\nChoose an option:\n").strip().lower()

        while choice not in ["a", "r", "c", "i", "o", "q"]:
            choice = input("Choose an option:\n").strip().lower()

        # add item
        if choice == "a":
            print("\nAdd your item to the cart")
            name = input("Enter the item name:\n").strip()
            description = input("Enter the item description:\n").strip()

            # price should be float greater than or equal to 0
            while True:
                try:
                    price = float(input("Enter the item price:\n"))
                    if price >= 0:
                        price = round(price, 2)
                        break
                except ValueError:
                    pass
                print("Invalid entry, please enter your price again")

            # quantity should be integer greater than 0
            while True:
                try:
                    qty = int(input("Enter the item quantity:\n"))
                    if qty > 0:
                        break
                except ValueError:
                    pass
                print("Invalid entry, please enter your quantity again")

            # call the class
            cart.add_item(ItemToPurchase(name, price, qty, description))

        # remove item
        elif choice == "r":
            print("\nRemove the item from your cart")
            name = input("Enter name of item to remove:\n").strip()
            cart.remove_item(name)

        # change item quantity
        elif choice == "c":
            print("\nChange the item quantity")
            name = input("Enter the item name:\n").strip()

            # quantity should be integer greater than or equal to 0
            while True:
                try:
                    qty = int(input("Enter the new quantity:\n"))
                    if qty >= 0:
                        break
                except ValueError:
                    pass
                print("Invalid entry, please enter your quantity again")

            cart.modify_item(ItemToPurchase(name=name, qty=qty))

        # output descriptions
        elif choice == "i":
            print("\nHere are item descrption")
            cart.print_descriptions()

        # output shopping cart
        elif choice == "o":
            print("\nHere is your shopping cart")
            cart.print_total()

        # quit
        elif choice == "q":
            print("\nYou have quit your cart.")


def main():

    # get prompt for name of custer and date
    name = input("Enter customer's name:\n").strip()
    date = input("Enter today's date:\n").strip()

    if name == "":
        name = "none"
    if date == "":
        date = "January 1, 2020"

    print(f"\nCustomer name: {name}")
    print(f"Today's date: {date}")

    cart = ShoppingCart(name, date)

    print_menu(cart)


if __name__ == "__main__":
    main()

