# Starter code for get_price


def get_price(fruits):
    """ This function gets the name of the most expensive fruit """
    inver_fruits = dict()
    for items , price in fruits.items():
        inver_fruits[price] = items
    max_price = max(inver_fruits)
    return inver_fruits[max_price]




# Create a dictionary of fruits manually
fruit = {"Orange": 2.0,"Apple":1.5,"Mango": 3.2,"Kiwi":1.2}
# Call the get_price function with the dictionary of fruits as an argument
max_name = get_price(fruit)
print(f'The most expensive fruit is: {max_name}')

