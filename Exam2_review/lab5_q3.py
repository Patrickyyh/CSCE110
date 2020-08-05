nba_champ = {'Boston Cletics':17, 'Minneapolis':16,"Chicao":6,'San Antonia':5,'New York Knicks':2 , 'Houston Rockets':2}
invert_champs = {}
for team , amount in nba_champ.items():
    invert_champs[amount] = invert_champs.get(amount,[]) + [team]

print(invert_champs)
print(sorted(invert_champs))
for key in sorted(invert_champs,reverse = True):
    print(key)
    for team in sorted(invert_champs[key],reverse=True):
       print(' ', team)
