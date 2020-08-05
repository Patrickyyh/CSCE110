def vertical_histogram(number_list):
    value = max(number_list)
    for number in number_list:
        count = 0
        for i in range(value):
            if count < number:
                print("*")






line = input("Enter a string of :  " ).split()
line_number = [int(n) for n in line]
vertical_histogram(line_number)