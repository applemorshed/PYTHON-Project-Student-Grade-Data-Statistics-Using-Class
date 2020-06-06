import csv
import json
import operator
import numpy as np
#from operator import attrgetter

src = open('studentFile.csv', "r+")
dst_csv_json = open("csvToJson.json", "w+")
dst_csv_json_gender_order = open("csvToJsonGenderOrdered.json", "w+")
ClassStats = open("csvToClassStats.json", "w+")

# Creating a Student Class which hold all the information


class Student:

    def __init__(self, FirstName: str, LastName: str, StudentID: float, StudentGrade: float, HomeTown: str, Gender: str):
        self.FirstName = FirstName
        self.LastName = LastName
        self.StudentID = StudentID
        self.StudentGrade = StudentGrade
        self.HomeTown = HomeTown
        self.Gender = Gender

    def __repr__(self):
        return '({},{},{},{},{},{})'.format(self.FirstName, self.LastName, self.StudentID, self.StudentGrade, self.HomeTown, self.Gender)


'''
def sort_gender(g):
    return g['Gender']
'''
# Answer to the Question No 2
#---------------------------------------------------------------#


def csvToList(src):
    src.seek(0, 0)
    next(src)
    lineReader = csv.reader(src)
    listfile = list(lineReader)
    # print(listfile)
    student_file = []
    for i in listfile:
        aa = Student(str(i[0]), str(i[1]), float(i[2]), float(i[3]), str(i[4]), str(i[5]))
        class_dict = aa.__dict__
        student_file.append(class_dict)
    print(student_file)

# Answer to the Question No 3
#---------------------------------------------------------------#


def csvToJson(src, dst):
    src.seek(0, 0)
    next(src)
    lineReader = csv.reader(src)
    listfile = list(lineReader)
    student_file = []
    for i in listfile:
        #print (i)
        aa = Student(str(i[0]), str(i[1]), float(i[2]), float(i[3]), str(i[4]), str(i[5]))
        # print(aa)
        class_dict = aa.__dict__
        student_file.append(class_dict)
    # print(student_file)
    json_str = json.dumps(student_file, indent=4)
    print(json_str)
    dst.write(json_str)
    dst.flush()

# Answer to the Question No 4
#---------------------------------------------------------------#


def csvToJsonGenderOrdered(src, dst, gender):
    src.seek(0, 0)
    next(src)
    lineReader = csv.reader(src)
    listfile = list(lineReader)
    # print(listfile)
    student_file = []
    for i in listfile:
        if i[5] == gender:
            student_file.append(i)

    # print(student_file)

    aa = []
    for i in student_file:
        #print (i)
        a_list = Student(str(i[0]), str(i[1]), float(i[2]), float(i[3]), str(i[4]), str(i[5]))
        aa.append(a_list)

    sorted_a = sorted(aa, key=operator.attrgetter('StudentGrade'), reverse=True)
    # print(sorted_a)
    a = []
    for i in sorted_a:
        # print(i)
        class_dict = i.__dict__
        a.append(class_dict)
    json_str = json.dumps(a, indent=4)
    print(json_str)
    dst.write(json_str)
    dst.flush()


# Answer to the Question No 1
#---------------------------------------------------------------#

def calculateClassStats(src, dst):
    src.seek(0, 0)
    next(src)
    lineReader = csv.reader(src)
    listfile = list(lineReader)
    # print(listfile)

    student_file = []
    for i in listfile:
        aa = Student(str(i[0]), str(i[1]), float(i[2]), float(i[3]), str(i[4]), str(i[5]))
        student_file.append(aa)
    # print(student_file)
    # a.remove("FirstName")
    # print(a)
    stat_list = {}

    grade_list = []  # All of the students grade
    for i in student_file:
        grade_list.append(i.StudentGrade)
    aveg_mean = np.mean(grade_list)

    # Male average and variance
    gender_list_M = []
    gender_list_grade = []
    for i in student_file:
        if i.Gender == 'M':
            gender_list_M.append(i)
    for i in gender_list_M:
        gender_list_grade.append(i.StudentGrade)
    male_avg = round(np.mean(gender_list_grade), 3)
    male_var = round(np.var(gender_list_grade), 3)

    # female average and standard deviation
    gender_list_F = []  # A list of female student
    gender_list_grade_F = []  # A list of female students grade
    for i in student_file:
        if i.Gender == 'F':
            gender_list_F.append(i)
    for i in gender_list_F:
        gender_list_grade_F.append(i.StudentGrade)
    female_avg = round(np.mean(gender_list_grade_F), 3)
    females_std = round(np.std(gender_list_grade_F), 3)

    # maximum student grade
    max_grade_student = []
    for i in student_file:
        if i.StudentGrade == np.max(grade_list):
            max_grade_student.append(i)
    min_grade_student = []
    for i in student_file:
        if i.StudentGrade == np.min(grade_list):
            min_grade_student.append(i)

    stat_list.update({'average': aveg_mean})
    stat_list.update({'male_average': male_avg})
    stat_list.update({'female_average': female_avg})
    for i in max_grade_student:
        stat_list.update({'max': str(i.StudentID)})
    for i in min_grade_student:
        stat_list.update({'min': str(i.FirstName) + " " + str(i.LastName)})
    stat_list.update({'males_var': male_var})
    stat_list.update({'females_std': females_std})
    if len(gender_list_M) > len(gender_list_F):
        stat_list.update({'greatest_gender': "BOY"})
    elif len(gender_list_M) < len(gender_list_F):
        stat_list.update({'greatest_gender': "GIRL"})
    else:
        stat_list.update({'greatest_gender': "EQUAL"})

    # print(stat_list)
    json_str = json.dumps(stat_list, indent=4)
    print(json_str)
    dst.write(json_str)
    dst.flush()


print("Answer to the Question No 1: ")
print(" ")
calculateClassStats(src, ClassStats)
print(" ")
print("Answer to the Question No 2: ")
print(" ")
csvToList(src)
print(" ")
print("Answer to the Question No 3: ")
print(" ")
csvToJson(src, dst_csv_json)
print(" ")
print("Answer to the Question No 4: ")
print(" ")
csvToJsonGenderOrdered(src, dst_csv_json_gender_order, 'M')


src.close()
dst_csv_json.close()
dst_csv_json_gender_order.close()
ClassStats.close()
