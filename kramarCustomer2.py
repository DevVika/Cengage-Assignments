"""
    Dont forget to include yap
"""

class KramarCustomer:
    def __init__ (self, number, name):
        self.number = number
        self.name = name
        self.orders = []

    def addOrder(self, order):
        self.orders.append(order)

    def __str__(self):
        result =  'Customer Name:      ' + self.name + '\n'
        result += 'Customer Number:    ' + self.number + '\n'
        result += 'Orders:\n'

        for order in self.orders:
            date = order[0]
            productCode = order[1]
            productName = order[2]
            pricePerItem = order[3]
            quantity = order[4]
            orderTotal = pricePerItem * quantity

            result += f"  Date: {date}\n"
            result += f"  Code: {productCode}\n"
            result += f"  Product: {productName}\n"
            result += f"  Qty: {quantity}\n"
            result += f"  Total: ${orderTotal:.2f}\n\n"

        return result
