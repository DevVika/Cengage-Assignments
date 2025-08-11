"""
    Program: kramarCustomer.py
    Author: Viktoriya Kramar
    Last modified: 8/11/2025

    This program defines the class of Kramar Customer, which displays all of
    the customer names and orders
"""

class KramarCustomer:
    def __init__ (self, number, name):
        # Initialize variables
        self.number = number
        self.name = name
        self.orders = []

    def addOrder(self, order):
        # Add the orders to display eventually
        self.orders.append(order)

    def __str__(self):
        # Displays everything from customeres
        result =  'Customer Name: ' + self.name + '\n'
        result += 'Customer Number: ' + str(self.number) + '\n'
        result += 'Orders:\n'

        # Grab everything from the tuple "order"
        for order in self.orders:
            date = order[0]
            productCode = order[1]
            productName = order[2]
            pricePerItem = order[3]
            quantity = order[4]
            orderTotal = pricePerItem * quantity

        # Display everything in the tuple
            result += f"  Date: {date}\n"
            result += f"  Product Code: {productCode}\n"
            result += f"  Product Name: {productName}\n"
            result += f"  Quantity: {quantity}\n"
            result += f"  Order Total: ${orderTotal:.2f}\n\n"

        return result
