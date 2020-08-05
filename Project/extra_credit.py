import csv
import matplotlib.pyplot as drawing
import os
import numpy as np
import matplotlib.pyplot as plt

"""
Name : extra_credit.py
Date : 08/02/2020
Author: QuanLin Yu
        Yuhao Ye
Email: yeyuhao1234@tamu.edu
       quanlin2019@tamu.edu
"""




def display():
    """
    Description : Display the Main Menu\n
    """
    print('*******************Main Menu*****************')
    print('1. Read CSV file of grades')
    print('2. Generate student report files')
    print('3. Generate student report charts')
    print('4. Generate class report file')
    print('5. Generate class report charts')
    print('6. Quit')
    print('************************************************')

def read_csv():
    """
    @ Author :Yuhao Ye\n
    Description: This function read the file which at specfic location\n
    return: a dictionary which store the scores of all students\n
    """
    student_info = dict()
    path = input("Enter the full path (absolute path ) of your csv file: ")
    try:
        with open(path, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                student_info[row['UIN']] = row
        print("File reads successfully!")
        print()
        return student_info
    except FileNotFoundError:
        print("Sorry cannot find your file, please read again.")
        print()






def grade_calculation(student_info,UIN):
    """
    @author Yuhao Ye\n
    param student_info:\n
    param UIN:\n
    Description: calculate Exam mean , labs mean , quizzes mean , Reading mean , Score as percentage  and Lettergrade\n
    return: student's final scores and grades\n
    """
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


def mean_calculation(object_type, amount,info_dict):
    """
    Author Yuhao Ye\n
    param object_type: type of grade (eg,Lab, quizz , exam ,project...)\n
    param amount: (eg, if there is 6 lab in total , the amount = 6)\n
    param info_dict:\n
    return: mean_value\n
    """
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



class Student:

    def __init__(self,UIN,student_info):
        self.uin = UIN
        self.student_info = student_info
        self.Score_percentage = 0
        self.student_final_grades = dict()
        self.letter_grade = ""
    def Generate_student_report(self):
        """
         @ Author : Yuhao Ye\n
         param student_info:\n
         Description  Generate student report\n
         return:\n
         """
        self.Score_percentage, self.student_final_grades = grade_calculation(self.student_info,self.uin)
        if self.Score_percentage >= 90:
            self.letter_grade = 'A'
        elif self.Score_percentage >= 80 and self.Score_percentage < 90:
            self.letter_grade = 'B'
        elif self.Score_percentage >= 70 and self.Score_percentage < 80:
            self.letter_grade = "C"
        elif self.Score_percentage >= 60 and self.Score_percentage < 70:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"
        File_name = self.uin+'.txt'
        with open(File_name, 'w') as write:
            write.write(f'Exams mean: {round(self.student_final_grades["Exams_mean"], 2)}\n')
            write.write(f'Labs mean: {round(self.student_final_grades["Labs_mean"], 2)}\n')
            write.write(f'Quizzes mean: {round(self.student_final_grades["Quizzes_mean"], 2)}\n')
            write.write(f'Reading activities mean: {round(self.student_final_grades["Reading_mean"], 2)}\n')
            write.write(f'Score: {round(self.Score_percentage, 2)}%\n')
            write.write(f'Letter grad: {self.letter_grade}\n')


    def Generate_student_chart(self):
        """
        @Author : YuHao Ye\n
        param student_info:\n
        Description : Generate report charts for student.\n
        return:\n
        """
        FIGURE1 = 1
        FIGURE2 = 2
        FIGURE3 = 3
        FIGURE4 = 4
        current_path = os.getcwd()
        new_path = current_path + f'\{self.uin}'
        if not os.path.exists(new_path):
            os.mkdir(new_path)
        os.chdir(new_path)

        #bar charts for exam
        drawing.figure(FIGURE1)
        student_grades = self.student_info.get(self.uin)
        exam_grade = list()
        for i in range(1, 4):
            target = 'exam ' + str(i)
            exam_grade.append(float(student_grades.get(target)))
        x_value = [1, 2, 3]
        drawing.title(f'Exam grade for {self.uin}', size=20)
        drawing.xlabel("Exam", size='15', color='red')
        drawing.ylabel("Scores %", size='15', color='red')
        drawing.yticks(range(0, 100, 10))
        drawing.bar(x_value, exam_grade)
        x_mark = 1
        for grade in exam_grade:
            drawing.text(x_mark - 0.05, grade + 0.5, grade, size="10")
            x_mark += 1
        drawing.savefig("exams_chart.png")

        # bar chart for lab
        drawing.figure(FIGURE2)
        lab_grade = list()
        for i in range(1, 7):
            target = 'lab ' + str(i)
            lab_grade.append(float(student_grades.get(target)))
        x_value = [1, 2, 3, 4, 5, 6]
        drawing.title(f'Lab grade for {self.uin}', size=20)
        drawing.xlabel('Lab', size='15', color='red')
        drawing.ylabel("Scores %", size='15', color='red')
        drawing.yticks(range(0, 120, 10))
        drawing.bar(x_value, lab_grade)
        x_mark = 1
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
        drawing.title(f'Quiz grade for {self.uin}', size=20)
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
        drawing.title(f'Reading activities grade for {self.uin}', size=10)
        drawing.xlabel('Reading activities', size='15', color='red')
        drawing.ylabel("Scores %", size='15', color='red')
        drawing.yticks(range(0, 120, 10))
        drawing.bar(x_value, reading_grade)
        x_mark = 1
        for grade in reading_grade:
            drawing.text(x_mark - 0.2, grade + 0.5, grade, size="10")
            x_mark += 1
        drawing.savefig("reading_chars.png")
        """:returns back to the previous work directory """
        os.chdir(current_path)







class Classroom:
    def __init__(self,student_info):
        self.info = student_info

    def Generate_class_report(self):
        '''
        @Author : QuanLin Yu\n
        param info: an ordered dictionary\n
        description: This function count weighted grade for every student and calculate mean and others parameters based on it\n
        return: None\n
        '''
        data = [0.15 * float(self.info[i]['exam 1']) + 0.15 * float(self.info[i]['exam 2']) + 0.15 * float(
            self.info[i]['exam 3']) + 0.25 * np.mean(np.array(
            [self.info[i]['lab 1'], self.info[i]['lab 2'], self.info[i]['lab 3'], self.info[i]['lab 4'], self.info[i]['lab 5'],
             self.info[i]['lab 6']], dtype=np.float32)) + 0.1 * np.mean(np.array(
            [self.info[i]['quiz 1'], self.info[i]['quiz 2'], self.info[i]['quiz 3'], self.info[i]['quiz 4'], self.info[i]['quiz 5'],
             self.info[i]['quiz 6']], dtype=np.float32)) + 0.1 * np.mean(np.array(
            [self.info[i]['reading 1'], self.info[i]['reading 2'], self.info[i]['reading 3'], self.info[i]['reading 4'],
             self.info[i]['reading 5'], self.info[i]['reading 6']], dtype=np.float32)) + 0.1 * float(self.info[i]['project']) for i in
                self.info]
        f = open('report.txt', 'w+')
        f.write('Number of students:{0}\n'.format(len(self.info)))
        f.write('Minimum score:{0}\n'.format(round(min(data), 1)))
        f.write('Maximum score:{0}\n'.format(round(max(data), 1)))
        f.write('Median score:{0}\n'.format(round(np.median(data), 1)))
        f.write('Mean score:{0}\n'.format(round(np.mean(data), 1)))
        f.write('Standard deviation:{0}\n'.format(round(np.std(data), 1)))
        f.close()

    def Generate_class_chart(self):
        '''
        @Author : QuanLin Yu\n
        param info: an ordered dictionary\n
        description: This function count weighted grade for every student and plot pie chart and histogram chart based on it\n
        return: None
        '''
        try:
            os.mkdir('class_charts')
        except FileExistsError:
            pass
        data = [0.15 * float(self.info[i]['exam 1']) + 0.15 * float(self.info[i]['exam 2']) + 0.15 * float(
            self.info[i]['exam 3']) + 0.25 * np.mean(np.array(
            [self.info[i]['lab 1'], self.info[i]['lab 2'], self.info[i]['lab 3'], self.info[i]['lab 4'],
             self.info[i]['lab 5'],
             self.info[i]['lab 6']], dtype=np.float32)) + 0.1 * np.mean(np.array(
            [self.info[i]['quiz 1'], self.info[i]['quiz 2'], self.info[i]['quiz 3'], self.info[i]['quiz 4'],
             self.info[i]['quiz 5'],
             self.info[i]['quiz 6']], dtype=np.float32)) + 0.1 * np.mean(np.array(
            [self.info[i]['reading 1'], self.info[i]['reading 2'], self.info[i]['reading 3'], self.info[i]['reading 4'],
             self.info[i]['reading 5'], self.info[i]['reading 6']], dtype=np.float32)) + 0.1 * float(
            self.info[i]['project']) for i in
                self.info]
        labels = ['A', 'B', 'C', 'D', 'F']
        grade = dict.fromkeys(labels, 0)
        for i in data:
            if 90 <= i <= 100:
                grade['A'] += 1
            elif 80 <= i < 90:
                grade['B'] += 1
            elif 70 <= i < 80:
                grade['C'] += 1
            elif 60 <= i < 70:
                grade['D'] += 1
            else:
                grade['F'] += 1
        grade = [i[1] for i in sorted(grade.items(), key=lambda x: x[0])]
        plt.pie(grade, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
        plt.title("class letter grades")
        plt.savefig("class_charts//class letter grades(pie).png")
        plt.clf()
        p1 = plt.bar(range(len(labels)), height=grade, width=0.5, tick_label=labels)
        for a, b in zip(range(len(labels)), grade):
            plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
        plt.xlabel("Grades")
        plt.ylabel("Count")
        plt.title("class letter grades")
        plt.savefig("class_charts//class letter grades(histogram).png")






def main():
    """
    @Author: QuanLin Yu\n
    """
     # this dict instore the information
    display()
    while True :
        try:
            options = int(input("Please enter an option (between 1-6  (Don't forget to read csv file at first! )): "))
        except ValueError:
            break
        if options == 6 :
            break
        else:
          if options == 1:
              student_info = read_csv()
          elif options == 2:
              while True:
                  UIN = input("Please enter the uin number: ")
                  if len(UIN) != 10:
                      print('The UIN must be ten digits !')
                  elif not UIN.isnumeric():
                      print('UIN must be all digits !')
                  elif UIN not in student_info:
                      print('The UIN you enter does not exits! ')
                  else:
                      break

              Student(UIN,student_info).Generate_student_report()

          elif options ==3 :
              while True:
                  UIN = input("Please enter the uin number: ")
                  if len(UIN) != 10:
                      print('The UIN must be ten digits !')
                  elif not UIN.isnumeric():
                      print('UIN must be all digits !')
                  elif UIN not in student_info:
                      print('The UIN you enter does not exits! ')
                  else:
                      break
              Student(UIN,student_info).Generate_student_chart()

          elif options == 4:
              Classroom(student_info).Generate_class_report()

          elif options == 5 :
              Classroom(student_info).Generate_class_chart()


        display()

if __name__ == '__main__':
    main()




