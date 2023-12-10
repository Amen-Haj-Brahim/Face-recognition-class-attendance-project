import csv
import pandas as pd
import re
import datetime
import time


def lst_of_students():
    lst=list()
    with open("Attendance_Table.csv") as file:
        reader=csv.DictReader(file)
        for row in reader:
            lst.append(row)
    return lst
#shows the final Attendance Table
def show_all_students():
    df=pd.read_csv("Attendance_Table.csv")
    print(df)
def update_attendance(student_lst):
    with open("Attendance_Table.csv", 'w', newline='') as file:
        writer = csv.DictWriter(file,['Student', 'Class', 'Attendance'])
        writer.writeheader()
        writer.writerows(student_lst)

def show_absent():
    lst=list()
    print("Absent Students:")
    with open("Attendance_Table.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Attendance"] == "Absent":
                lst.append(row)
    for dict in lst:
        print(f"Student : {dict['Student']} | Class : {dict['Class']}")
def show_attended():
    lst=list()
    print("Present Students:")
    with open("Attendance_Table.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Attendance"] == "Present":
                lst.append(row)
    for dict in lst:
        print(f"Student : {dict['Student']} | Class : {dict['Class']}")

def teacher_menu():
    choice = None
    while (choice != 4):
        print("1-Show all students:")
        print("2-Show Absent Students:")
        print("3-Show Present Students")
        print("4-Quit")
        choice = input("enter your choice:")
        if re.fullmatch("[1-4]",choice):
            match choice:
                case '1':
                    show_all_students()
                case '2':
                    show_absent()
                case '3':
                    show_attended()
                case '4':
                    break
        else:
            print('wrong input!')
