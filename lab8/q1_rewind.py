
def grade_calculator(exam1 ,exam2, exam3):
   """This function return total value and letter grade """
   total = 0.25*exam1 + 0.35 * exam2 + 0.4 * exam3
   total = round(total,2)
   if total < 60:
       grade = 'F'
   elif total < 70:
       grade = 'D'
   elif total < 80:
       grade = 'C'
   elif total < 90:
       grade = 'B'
   else:
       grade = 'A'

   return total, grade




filename = 'exam_scores.txt'
with open(filename,'r')as f:
   scores_list = f.read()


scores_list = scores_list.split("\n")
print(scores_list)
"""grade_list store the string information of """
grade_list = []
"""score_dict store the total points"""
score_dict = {}
"""score_dict store the grade"""
grade_dict = {}
i = 1
for score in scores_list:
    score = score.split()
    student_id = int(score[0])
    exam1 = int(score[1])
    exam2 = int(score[2])
    exam3 = int(score[3])
    total_points , grade = grade_calculator(exam1,exam2,exam3)
