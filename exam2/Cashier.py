# Starter code for cashier


def cashier(items):
    ''' This function reads grocery items and prints a receipt '''
    basket = {}  # Empty dictionary that will store the items
    # Write the body of this function
    total_price = 0
    for i  in range(items):
        item = input('Item name: ')
        price = float(input('Item price: '))
        basket[item] = price
        print()

    for price in basket.values():
        total_price += price


    with open('receipt.txt','w') as write_in:
        write_in.write('Receipt:\n')
        for item,price in basket.items():
            line = f'{item}: ${price}\n'
            write_in.write(line)
        line_last = f'Your total is ${total_price}, Thank you!\n'
        write_in.write(line_last)



items = int(input("Number of items: "))  # Ask for the number of items
print()
cashier(items)  # Call to the cashier function
