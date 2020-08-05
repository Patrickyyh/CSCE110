line1  = list()
line2 = list()
with open("line1","r") as read:
    line1= read.read().split(",")



with open("line2","r") as read:
    line2 = read.read().split(",")


print(line1)
print(line2)
flag = 0
count = 0
while(True):

    if count<=len(line1)-1:
        print(line1[count])
    else:
        flag+=1


    if count <= len(line2)-1:
        print(line2[count])
    else:
        flag+=1
    if flag == 2:
        break

    count +=1


