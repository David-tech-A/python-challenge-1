# 🍔 Food Truck Ordering System

## Overview

This Python script implements an interactive ordering system for a food truck menu. It allows customers to select items, specify quantities, and generates a formatted receipt.

## Features

- **Interactive Menu**: Displays a menu of food items with prices.
- **User Input Validation**: Ensures correct input for menu selection and quantity.
- **Dynamic Order Management**: Allows multiple item orders with varying quantities.
- **Formatted Receipt**: Generates a neatly formatted receipt with item details and total price.

## How to Use

1. Run the script in a Python environment.
2. Follow the prompts to select menu items and quantities.
3. Choose to continue ordering or finish your order.
4. Review the generated receipt.

## Code Structure

The main components of the system are:

- `order`: A list to store the customer's order.
- `menu_items`: A dictionary containing the menu items and their prices.
- `display_menu()`: Function to display the menu.
- `get_valid_int()`: Function for input validation.
- Main ordering loop with input processing and order management.
- Receipt generation and total calculation.

## Sample Output

> Your Order:
> Item name                 | Price  | Quantity
> --------------------------|--------|----------
> Burger                    | $5.99  | 2
> Fries                     | $2.99  | 1
> Soda                      | $1.99  | 3
> 
> Total: $20.95


*Enjoy your meal! 🌮🥤*
