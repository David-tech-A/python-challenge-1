# Initialize an empty list to store the customer's order
order = []

# Define the menu items with their names and prices
menu_items = {
    1: {"name": "Burger", "price": 5.99},
    2: {"name": "Fries", "price": 2.99},
    3: {"name": "Soda", "price": 1.99},
    4: {"name": "Hot Dog", "price": 3.99},
    5: {"name": "Pizza Slice", "price": 4.99}
}

def display_menu():
    """Display the food truck menu to the customer."""
    print("\nMenu:")
    for key, item in menu_items.items():
        print(f"{key}. {item['name']} - ${item['price']:.2f}")

def get_valid_int(prompt):
    """
    Get a valid integer input from the user.
    
    Args:
        prompt (str): The input prompt to display to the user.
    
    Returns:
        int: A valid integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main ordering loop
place_order = True
while place_order:
    display_menu()
    
    # Get menu selection from the customer
    menu_selection = get_valid_int("Enter your selection (1-5): ")
    
    # Validate the menu selection
    if menu_selection not in menu_items:
        print("Error: Invalid menu selection.")
    else:
        # Get the selected item details
        item = menu_items[menu_selection]
        item_name = item["name"]
        
        # Get the quantity of the selected item
        quantity = get_valid_int(f"How many {item_name}(s) would you like? (Default is 1): ")
        if quantity < 1:
            print("Invalid quantity. Setting to 1.")
            quantity = 1
        
        # Add the selected item to the order
        order.append({
            "Item name": item_name,
            "Price": item["price"],
            "Quantity": quantity
        })
        
        print(f"{quantity} {item_name}(s) added to your order.")
    
    # Ask if the customer wants to keep ordering
    while True:
        keep_ordering = input("Would you like to order anything else? (y/n): ").lower()
        match keep_ordering:
            case 'y':
                break
            case 'n':
                place_order = False
                print("Thank you for your order.")
                break
            case _:
                print("Invalid input. Please enter 'y' or 'n'.")

# Print receipt
print("\nYour Order:")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# Loop through each item in the order and print its details
for item in order:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]
    
    # Calculate spaces for formatting
    name_spaces = " " * (25 - len(item_name))
    price_spaces = " " * (6 - len(f"{price:.2f}"))
    
    # Print the item details in a formatted manner
    print(f"{item_name}{name_spaces} | ${price:.2f}{price_spaces} | {quantity}")

# Calculate and display the total price of the order
total = sum(item["Price"] * item["Quantity"] for item in order)
print(f"\nTotal: ${total:.2f}")
