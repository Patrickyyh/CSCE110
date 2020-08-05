import matplotlib.pyplot as drawing

import random
quizz = ['quiz 1' , 'quiz 2' , 'quiz 3' , 'quiz 4' , 'quiz 5','quiz 6']
grades = [98,75,42,69,76,82]
bar = drawing.barh(quizz , grades)
print(bar)
drawing.xlabel('Quiz numbers')
drawing.ylabel('Grades')
drawing.title('CSCE 110 grades')
for n in range(len(bar)):
    color = random.choice(['b','r','y','g','m','c'])
    bar[n].set_color(color)

drawing.show()