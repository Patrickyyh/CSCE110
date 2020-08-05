# displays the main menu
import csv
"""import csv to read csv file into the dictionary """
import matplotlib.pyplot as drawing
"""import matplotlib to draw the corresponding plot"""
import os
"""import os to make directories """

def display():
    """display the main menue"""
    print('*******************Main Menu*****************')
    print('1. Read CSV file of grades')
    print('2. Generate student report files')
    print('3. Generate student report charts')
    print('4. Generate class report file')
    print('5. Generate class report charts')
    print('6. Quit')
    print('************************************************')


def read_csv():
  student_info = dict()
  total_lab = 0
  with open("C:\\Users\\e3270\\Downloads\\grades.csv",'r') as file:
      csv_file = csv.DictReader(file)
      for row in csv_file:
         student_info[row['UIN']] = row
  return student_info


def grade_calculation(student_info,UIN):
    """calculate the final scores and letter grade for each student"""
    student_final_grade = dict()

    for uin, values in student_info.items():
        if uin == UIN:
            student_final_grade['Labs_mean']      = mean_calculation('lab', 6, values)
            student_final_grade['Exams_mean']     = mean_calculation('exam', 3, values)
            student_final_grade['Quizzes_mean']   = mean_calculation('quiz', 6, values)
            student_final_grade['Reading_mean']   = mean_calculation('reading', 6, values)
            student_final_grade['Project_grade']  = mean_calculation('project', 1, values)
    Scores_percentage = student_final_grade['Labs_mean']  * 0.25 + student_final_grade['Exams_mean']* 0.45 + student_final_grade['Quizzes_mean']  * 0.1 +\
                        student_final_grade['Reading_mean'] * 0.1 + \
                        student_final_grade['Project_grade'] * 0.1
    return Scores_percentage,student_final_grade

def Generate_student_report(student_info):
    """Function Generage_student_report create student report : Options 2 """
    while True:
       UIN = input("Please enter the uin number: ")
       if len(UIN) != 10:
          print('The UIN must be ten digits !')
       elif  not UIN.isnumeric():
          print('UIN must be all digits !')
       elif UIN not in student_info:
          print('The UIN you enter does not exits! ')
       else:
           break

    Scores_percentage, studetn_final_grades= grade_calculation(student_info,UIN)

    if Scores_percentage >= 90:
        grade_lettter = 'A'
    elif Scores_percentage >= 80 and Scores_percentage < 90:
        grade_lettter = 'B'
    elif Scores_percentage >= 70 and Scores_percentage< 80:
        grade_lettter = "C"
    elif Scores_percentage >= 60 and Scores_percentage < 70:
        grade_lettter = "D"
    else:
        grade_lettter = "F"

    """Write the result into the UIN.txt"""
    File_name = UIN+'.txt'
    with open(File_name,'w') as write:
        write.write(f'Exams mean: {round(studetn_final_grades["Exams_mean"],2)}\n')
        write.write(f'Labs mean: {round(studetn_final_grades["Labs_mean"],2)}\n')
        write.write(f'Quizzes mean: {round(studetn_final_grades["Quizzes_mean"],2)}\n')
        write.write(f'Reading activities mean: {round(studetn_final_grades["Reading_mean"],2)}\n')
        write.write(f'Score: {round(Scores_percentage,2)}%\n')
        write.write(f'Letter grad: {grade_lettter}\n')

    print('The student report has been created successfully , you will see it after quiting ')
    print()


#This function takes three parameters:
# object_type: accpet the type of the grade ex: (lab , quizz , project)
# amount:accept the amount of the grade : for example,if you take 7 labs total , then pass 7
# info_dict, pass the dict that stores the information of all the students
def mean_calculation(object_type, amount,info_dict):
    """Calculating the mean """
    total_scores = 0
    mean_value = 0
    # since there is only one project, hence return project grade instantly
    if object_type == "project":
       return  float(info_dict['project'])

    else:
       for number in range(1, amount + 1 ):
          type_name = object_type
          type_name = type_name + " "  + str(number)
          total_scores = total_scores + float(info_dict[type_name])
       mean_value = total_scores / amount
       return mean_value
    """Calculating the mean """


def generate_stuent_chart(student_info):
    """generate the chart : options:3 """
    FIGURE1 = 1
    FIGURE2 = 2
    FIGURE3 = 3
    FIGURE4 = 4
    current_path = os.getcwd()
    while True:
        UIN_Number = input("Please enter the uin number: ")
        if len(UIN_Number ) != 10:
            print('The UIN must be ten digits !')
        elif not UIN_Number .isnumeric():
            print('UIN must be all digits !')
        elif UIN_Number  not in student_info:
            print('The UIN you enter does not exits! ')
        else:
            break
    #creat the directory where stores the the report chart
    new_path = current_path+f'\{UIN_Number}'

    if not os.path.exists(new_path):
        os.mkdir(new_path)
    os.chdir(new_path)

    #bar charts for exam
    student_grades = student_info.get(UIN_Number)
    exam_grade = list()
    for i in range(1, 4):
        target = 'exam ' + str(i)
        exam_grade.append(float(student_grades.get(target)))
    drawing.figure(FIGURE1)
    x_value = [1 , 2 , 3]
    drawing.title(f'Exam grade for {UIN_Number}',size = 20)
    drawing.xlabel("Exam",size ='15' , color = 'red')
    drawing.ylabel("Scores %",size = '15', color = 'red')
    drawing.yticks(range(0,100,10))
    drawing.bar(x_value,exam_grade)
    x_mark = 1
    for grade in exam_grade:
      drawing.text(x_mark-0.05,grade+0.5,grade,size = "10")
      x_mark+=1
    drawing.savefig("exams_chart.png")


#bar chart for lab
    drawing.figure(FIGURE2)
    lab_grade = list()
    for i in range(1,7):
        target = 'lab ' + str(i)
        lab_grade.append(float(student_grades.get(target)))
    x_value = [1,2,3,4,5,6]
    drawing.title(f'Lab grade for {UIN_Number}',size = 20)
    drawing.xlabel('Lab' , size = '15',color = 'red')
    drawing.ylabel("Scores %",size = '15', color = 'red')
    drawing.yticks(range(0, 120, 10))
    drawing.bar(x_value, lab_grade)
    x_mark =1
    for grade in lab_grade:
        drawing.text(x_mark - 0.07, grade + 0.5, grade, size="10")
        x_mark += 1
    drawing.savefig("lab_chars.png")

# bar chart for quiz
    drawing.figure(FIGURE3)
    quiz_grade = list()
    for i in range(1, 7):
        target = 'quiz ' + str(i)
        quiz_grade.append(float(student_grades.get(target)))
    x_value = [1, 2, 3, 4, 5, 6]
    drawing.title(f'Quiz grade for {UIN_Number}', size=20)
    drawing.xlabel('Quiz', size='15', color='red')
    drawing.ylabel("Scores %", size='15', color='red')
    drawing.yticks(range(0, 120, 10))
    drawing.bar(x_value, quiz_grade)
    x_mark = 1
    for grade in quiz_grade:
        drawing.text(x_mark - 0.2, grade + 0.5, grade, size="10")
        x_mark += 1
    drawing.savefig("quiz_chars.png")

# bar chart for reading activities
    drawing.figure(FIGURE4)
    reading_grade = list()
    for i in range(1, 7):
        target = 'reading ' + str(i)
        reading_grade.append(float(student_grades.get(target)))
    x_value = [1, 2, 3, 4, 5, 6]
    drawing.title(f'Reading activities grade for {UIN_Number}', size=10)
    drawing.xlabel('Reading activities', size='15', color='red')
    drawing.ylabel("Scores %", size='15', color='red')
    drawing.yticks(range(0, 120, 10))
    drawing.bar(x_value, reading_grade)
    x_mark = 1
    for grade in reading_grade:
        drawing.text(x_mark-0.2 , grade+0.5, grade, size="10")
        x_mark += 1
    drawing.savefig("reading_chars.png")
    """:returns back to the previous work directory """
    os.chdir(current_path)


student_info = dict()  # this dict instore the information
"""store every student'grade """

# This is the main function, you could create the function and put them into the fllowing conditions:
def main():

    display()
    while True :
      options = int(input("Please enter an option (between 1-6  (Don't forget to read csv file at first! )): "))

      if options == 6 :
          break
      else:
          if options == 1:
              student_info = read_csv()
          elif options == 2:
              Generate_student_report(student_info)
          elif options ==3 :
              generate_stuent_chart(student_info)
          elif options == 4:
              pass
          elif options == 5 :
             pass
      display()

if __name__ == '__main__':
    main()
