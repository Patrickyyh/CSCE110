number_item = int(input("Number of items: "))
print()
item_dict = dict()
total_price = 0
for num in range(number_item):
   name = input("Item name : ")
   price = input("Item price: ")
   item_dict[name] = price
   print()


new_itemdict = sorted(item_dict,reverse= True)


print("Receipt:")
for name in new_itemdict:
    print(f'{name}: ${item_dict[name]}')
    total_price += float(item_dict[name])

print(f'You total is ${total_price}, Thank you!')