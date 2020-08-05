number_order = []
new_major = []
majors = ['stats', 'eng', 'math', 'cs']
for major in majors:
    number_order.append(len(major))


number_order.sort()
print(number_order)


for order in number_order:
    for major in majors:
        if len(major) == order:
            new_major.append(major)


majors = new_major
print(majors)