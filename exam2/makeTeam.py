import random
names = ["Ashley", "Sam", "Anna", "Tim", "Kate"]


def make_team(names, size):
    ''' This function makes a list of random team members '''
    # Write the body of this function
    if size > len(names):
        print("The team size is too large")
        return 0
    else:
        team_choice = random.sample(names,size)
        return  team_choice


team = ["Ashley", "Sam", "Anna", "Tim", "Kate"]
    # Ask for the team size
size = int(input('Enter the team size: '))
    # Call the make_team function
choice = make_team(team,size)
if choice != 0:
     print(f'The team is {choice}')