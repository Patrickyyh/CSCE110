with open('tree.txt') as trees_data:
    trees = trees_data.readlines()
    # remove the special character over here
    trees = [name.strip() for name in trees]
    tree_count = {}
    for tree in trees:
        tree_count[tree] = trees.count(tree)

print(tree_count)
tree_count_sorted = {}
for tree in sorted(tree_count):
    tree_count_sorted[tree] = tree_count[tree]
print(tree_count_sorted)


with open('trees-stats.txt','w')as trees_stats:
    for name , count in tree_count_sorted.items():
        trees_stats.write(f'The count of {name} is {count}\n')
if (not trees_stats.closed):
    trees_stats.close()
else:
    print(f"The trees_stats has already been closed")