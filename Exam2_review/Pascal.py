rows = int(input("Rows: "))
print()
line = list(["1"])
print_line = (["1"])
for number in range(rows):
    if number < 1:
       line.append(str(number))
       print(" ".join(line))
       line = list(["1"])
    elif number == 1:
       line.append(str(number))
       for n in range(len(line)-1):
           print_line.append(str(int(line[n]) + int(line[n+1])))
    else:
       print_line.append('1')
       print(" ".join(print_line))
       temp_line = print_line
       print_line = (["1"])
       for n in range(len(temp_line) -1):
           print_line.append(str(int(temp_line[n]) + int(temp_line[n+1])))













