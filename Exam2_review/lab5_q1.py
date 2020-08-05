sequence = input("Enter a Sentence: ").lower()
print(sequence)
stat = {}
for word  in sequence:
    if word.isalpha():
       if word in stat:
           stat[word] +=1
       else:
           stat[word]=1

print(stat)

inv_stats = {}
for letter , count in stat.items():
    ##Optional. A value to return if the specified key does not exist.Default value None
    inv_stats[count] = inv_stats.get(count,[]) + [letter]
print(inv_stats)

for i in sorted(inv_stats,reverse=True):
    chars = inv_stats[i]
    for char in sorted(chars):
        print(f'{char} appeared {i} times')


