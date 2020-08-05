# File: q1.py
# Author: Yuhao Ye
# Date: 07/25/2020
# Section: 529006730
# E-mail: yeyuhao1234@tamu.edu
# Description:
#  reads the data of the file, calculates the total score and letter grade for each student, and
#  generates three text files grades.txt,
#  sorted_ids.txt and sorted_grades.txt




## read all the data into the dict info_store
with open("exam_scores.txt",'r') as read:
    info_store = dict()
    line = read.readline().strip()
    while line != "":
     line = line.split(" ")
     for info in line[1:]:
         info_store[line[0]] = info_store.get(line[0],[]) + [float(info)]
     line  = read.readline().strip()



## calculate the scores
info = dict()
for id , score in info_store.items():
    avg = sum(score) / 3
    grade_lettter = "null"
    if avg >= 90 :
        grade_lettter = 'A'
    elif  avg>=80 and avg < 90:
        grade_lettter = 'B'
    elif avg >=70 and avg <80:
        grade_lettter = "C"
    elif avg >= 60 and avg < 70:
        grade_lettter = "D"
    else:
        grade_lettter = "F"
    info[id] = info.get(id,[]) + [avg]
    info[id] = info.get(id , []) + [grade_lettter]

# grades.txt
with open('grades.txt','w')as write:
    for id , grades in info.items():
        line = f'ID:{id} has a score of {round(info.get(id)[0],2)}, Letter grade: {info.get(id)[1]}\n'
        write.write(line)

#sorted_ids.txt
with open('sorted_ids.txt','w')as write:
    for id , grades in sorted(info.items()):
        line = f'ID:{id} has a score of {round(info.get(id)[0],2)}, Letter grade: {info.get(id)[1]}\n'
        write.write(line)
#sorted_grades.txt
with open('sorted_grades.txt','w')as write:
    for grades in sorted(info.values()):
        for id in info.keys():
          if info.get(id) == grades:
             line = f'ID:{id} has a score of {round(info.get(id)[0],2)}, Letter grade: {info.get(id)[1]}\n'
             write.write(line)