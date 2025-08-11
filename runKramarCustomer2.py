from kramarCustomer import KramarCustomer

"""
    Program: runKramarCustomer.py
    Author: Viktoriya Kramar
    Last modified: 8/11/2025

    This program defines the functions, a dictionary, and a tuple in order
    to loop through the files and gather customer information
    
"""

def readCustomers():
    # Open file and read
    f = open("customers.txt", 'r')

    # Dictionary holds customer's name and number
    customers = {}

    for line in f:
        items = line.split(',')
        number = int(items[0].strip())
        name = items[1].strip()
        c = KramarCustomer(number, name)
        customers[number] = c
    f.close()
    return customers
            

def readOrders(customers):
    # Open and read file
    f = open("orders.txt", 'r')

    for line in f:
        items = line.split(',')
        number = int(items[0].strip())
        # If customer exists in the dictionary
        if customers.get(number) is not None:
            # Get the customer object
            customer = customers.get(number)
            date = items[1].strip()
            productCode = items[2].strip()
            productName = items[3].strip()
            pricePerItem = float(items[4].strip())
            quantity = int(items[5].strip())
            order = (date, productCode, productName, pricePerItem, quantity)
            customer.addOrder(order)
    f.close()
    

def main():
    customers = readCustomers()
    readOrders(customers)
    print("Genco Pura Olive Oil Customer List")
    # Loop through customers and print using str
    for c in customers:
        print(customers[c])
        

if __name__ == "__main__":
    main()