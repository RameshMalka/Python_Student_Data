import pandas as pd
import os


def student_details_header():
    eachstudent = open('students_file.csv', 'a')
    # if eachstudent.readline() == '':
    # os.path.getsize('yourfile.csv')
    # if eachstudent.read() == '':
    if os.path.getsize('students_file.csv') == 0:
        eachstudent.write('StudentID' + ',')
        eachstudent.write('FirstName' + ',')
        eachstudent.write('LastName' + ',')
        eachstudent.write('Major' + ',')
        eachstudent.write('Phone' + ',')
        eachstudent.write('GPA' + ',')
        eachstudent.write('DOB' + '\n')


# student_details_header()


def student_data():
    print('Do you want to Student details? ')
    another_student = input('y = yes, anything else = no: ')

    eachstudent = open('students_file.csv', 'a')
    while another_student == 'y' or another_student == 'Y':
        StudentID = int(input('Enter Student ID: '))
        eachstudent.write(str(StudentID) + ',')
        FirstName = input('Enter Student First Name: ')
        eachstudent.write(FirstName + ',')
        LastName = input('Enter Last Name: ')
        eachstudent.write(LastName + ',')
        Major = input('Enter Student Majors: ')
        eachstudent.write(Major + ',')
        Phone = int(input('Enter Phone number: '))
        eachstudent.write(str(Phone) + ',')
        GPA = float(input("Enter Student's GPA: "))
        eachstudent.write(str(GPA) + ',')
        DOB = input("Enter Student's Date of Birth: ")
        eachstudent.write(DOB + '\n')

        print('Do you want to add another Student? ')
        another_student = input('y = yes, anything else = no: ')
    eachstudent.close()
    print('Entered data is appended to names.txt')


# student_data()


def display_Student_data():
    # read_student_data = open('students_file.csv', 'r')
    # print('Student details below:')
    # print(read_student_data.read())

    # dataframe_read_student = pd.read_csv('students_file.csv', index_col=0)
    dataframe_read_student = pd.read_csv('students_file.csv')
    print('Student details below using dataframes:')
    print(dataframe_read_student)

    # read_student_data.close()


# display_Student_data()


def sort_student_dataframe():
    df_student_info = pd.read_csv('students_file.csv')

    print("1 - To sort Student Information based on First Name")
    print("2 - To sort Student Information based on Last Name")
    print("3 - To sort Student Information based on Majors")
    sort_condition = int(input("Enter the sort condition"))

    if sort_condition == 1:
        print('sorted student info by firstname')
        print(df_student_info.sort_values('FirstName'))

    elif sort_condition == 2:
        print('sorted student info by Last Name')
        print(df_student_info.sort_values('LastName'))

    elif sort_condition == 3:
        print('sorted student info by Major')
        print(df_student_info.sort_values('Major'))

    else:
        print("Invalid input")


# sort_student_dataframe()


def search_student_dataframe():
    df_student_info = pd.read_csv('students_file.csv')
    search_StudentID = int(input('Enter searching Student ID: '))
    print(df_student_info.loc[df_student_info['StudentID'] == search_StudentID])

    search_LastName = input('Enter searching Last Name: ')
    print(df_student_info.loc[df_student_info['LastName'] == search_LastName])
    search_Major = input('Enter searching Majors: ')
    print(df_student_info.loc[df_student_info['Major'] == search_Major])


# search_student_dataframe()


def main():
    student_details_header()

    while True:
        print("Menu Options: ")
        print("1 - To add a new Student data")
        print("2 - To display data of all Students")
        print("3 - To display sorted Student Information")
            # print("1 - To sort Student Information based on First Name")
            # print("1 - To sort Student Information based on Last Name")
            # print("1 - To sort Student Information based on Majors")
        print("4 - To search for specific Student Information")
            # print("1 - To search for specific Student Information based on First Name")
            # print("1 - To search for specific Student Information based on Last Name")
            # print("1 - To search for specific Student Information based on Majors")
        print("5 - To modify Student data")
            ########asf
            ###

        print("6 - To exit")

        user_choice = int(input("Enter your choice:"))

        if user_choice == 1:
            student_data()

        elif user_choice == 2:
            display_Student_data()

        elif user_choice == 3:
            sort_student_dataframe()

        elif user_choice == 4:
            search_student_dataframe()

        elif user_choice == 5:
            #print("asf")
            print("yet to add details")

        elif user_choice == 6:
            break

        else:
            print("Invalid input")


main()
