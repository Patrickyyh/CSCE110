number_item = int(input("Number of items: "))
print()
item_dict = dict()
total_price = 0
for num in range(number_item):
   name = input("Item name : ")
   price = input("Item price: ")
   item_dict[name] = price
   print()


print("Receipt:")
for name,price in item_dict.items():
    print(f'{name}: ${price}')
    total_price += float(price)

print(f'You total is ${total_price}, Thank you!')