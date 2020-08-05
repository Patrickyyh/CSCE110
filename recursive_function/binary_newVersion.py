def findSomething(list , item, low , high ):
    range_size = high - low  + 1
    mid = (high + low) // 2
    if item == list[mid]:
        pos = mid

    elif range_size == 1:
        pos = -1

    else:
        if item < list[mid] :
           pos = findSomething(list, item,low, mid)
        else:
           pos = findSomething(list,item,mid+1 ,high)
    return pos

attendees = []
attendees.append(1)
attendees.append(2)
attendees.append(12)
attendees.append(19)
print(attendees)
print(findSomething(attendees,12,0,len(attendees)-1))
