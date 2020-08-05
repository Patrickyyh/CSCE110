def wobbly(number):
    number = list([int(n)for n in number])
    flag_bigger = 0
    flage_smaller = 0
    for n in range(len(number)-1):
        if number[n] > number[n+1]:
           flage_smaller = 0
           flag_bigger +=1
        else:
            flag_bigger =0
            flage_smaller +=1
        if flag_bigger == 2 or flage_smaller == 2:
            return False
    return True








print(wobbly("19284756242"))
print(wobbly("89012345"))
print(wobbly("0909"))