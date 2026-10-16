import csv


class Student:
    def __init__(self, student_id, name, conduct_score, midterm, final):
        self.student_id = student_id
        self.name = name
        self.conduct_score = conduct_score
        self.midterm = midterm
        self.final = final
        self.total = 0.0

    def calculate_total(self):
        self.total = self.midterm * 0.3 + self.final * 0.7

    def scholarship_rank(self):
        if self.total >= 9 and self.conduct_score >= 90:
            return "A"
        elif self.total >= 8 and self.conduct_score >= 80:
            return "B"
        elif self.total >= 7 and self.conduct_score >= 70:
            return "C"
        return "None"

def sort_by_total(student_list):
    return sorted(student_list, key=lambda s: s.total, reverse=True) # sort tu tren xuong


def print_all(student_list):
    for s in student_list:
        print(s.student_id, s.name, s.total, 2), s.scholarship_rank()
#dict
def read_students(file_name):
    students = []
    with open(file_name,'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            s = Student(row["studentID"],row["Name"],float(row["conduct_score"]),float(row["midterm"]),float(row["final"]),)
            s.calculate_total()
            students.append(s)
            #print(row)
    return students
#list
def read_students_list(file_name):
    students = []
    with open(file_name,'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            s = Student(row[0],row[1],float(row[2]),float(row[3]),float(row[4]),)
            s.calculate_total()
            students.append(s)
            #print(row)
    return students


def give_scholarship(student_list , lenght = 0.12):
    ranked = sort_by_total(student_list)
    so_luong = max(1, int(len(ranked) * lenght))   # lay 12%
    print("danh sach sinh vien duoc hoc bong:")
    for s in range(0, so_luong): 
        if ranked[s].scholarship_rank() != "None":
            print(ranked[s].student_id, ranked[s].name, ranked[s].total, ranked[s].scholarship_rank())

students2 = read_students_list("data.csv")
#=============================================================================
students = read_students("data.csv")
#give_scholarship(students)
#print_all(students)
