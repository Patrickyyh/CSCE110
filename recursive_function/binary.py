def find(low,high):
    mid = (high + low) // 2
    answer = input(f'is it {mid} ?')
    if (answer != 'l') and (answer != 'h'):
        print("Congratulation! ")
    else:
        if answer == "l":
            find(low,mid)
        else:
            find(mid+1,high)


print('Choose a number from 0 to 100.')
find(0,100)
"""
why the binary search has a high efficiency
1. reducing the search space 
2. The search terminates when the target element is found 
 

"""