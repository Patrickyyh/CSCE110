#roster = set(list(range(10)))
#print(roster)
#roster = input("Enter numbers: ").split(sep=',')
###efficient way to conver string in a set to the int number:
#roster =[int(n) for n in roster]
roster = {1,2,3,4,5,6}
print(roster)

roster.discard(4)
print(roster)


roster.remove(6)
print(roster)


roster.discard(13)