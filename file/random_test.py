import random
#return the a random number between the 0.0 but not 1.0
print(random.random())
#randint() including the low and high
#randrange() not inlcluding the high one
## choice
#uniform return a random floating point number between a and b inclusive
# both inclusive
#getrandbits(k)

t = [1,2,3,4,5]
print(random.choice(t))
print(random.shuffle(t))
print(t)
## sample
print(random.sample(t,3))
print(random.getstate())