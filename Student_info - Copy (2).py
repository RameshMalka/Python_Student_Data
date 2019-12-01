from datetime import date

import pandas as pd
import os


def student_details_header():
    eachstudent = open('students_file.csv', 'a')
    if os.path.getsize('students_file.csv') == 0:
        eachstudent.write('STUDENTID' + ',')
        eachstudent.write('FIRSTNAME' + ',')
        eachstudent.write('LASTNAME' + ',')
        eachstudent.write('MAJOR' + ',')
        eachstudent.write('PHONE' + ',')
        eachstudent.write('GPA' + ',')
        eachstudent.write('DOB' + '\n')

    eachstudent.close()


# student_details_header()


def student_data():
    another_student = 'y'

    eachstudent = open('students_file.csv', 'a')
    while another_student == 'y' or another_student == 'Y':
        STUDENTID = int(input('Enter Student ID: '))
        eachstudent.write(str(STUDENTID) + ',')
        FIRSTNAME = input('Enter Student First Name: ')
        eachstudent.write(FIRSTNAME + ',')
        LASTNAME = input('Enter Last Name: ')
        eachstudent.write(LASTNAME + ',')
        Major = input('Enter Student Majors: ')
        eachstudent.write(Major + ',')
        Phone = int(input('Enter Phone number: '))
        eachstudent.write(str(Phone) + ',')
        GPA = float(input("Enter Student's GPA: "))
        eachstudent.write(str(GPA) + ',')
        isValidDate = True
        while isValidDate:
            isValidDate = False
            DOB = input("Enter Student's Date of Birth in 'dd/mm/yyyy' format: ")
            import datetime
            day, month, year = DOB.split('/')
            try:
                datetime.datetime(int(year), int(month), int(day))
            except ValueError:
                print("Input date is Invalid..Try again")
                isValidDate = True
            if not isValidDate:
                DOBS = date(int(year), int(month), int(day))
                eachstudent.write(str(DOBS) + '\n')
        print('Do you want to add another Student? ')
        another_student = input('y = yes, anything else = no: ')
    eachstudent.close()


# student_data()


def display_Student_data():
    dataframe_read_student = pd.read_csv('students_file.csv')
    print('Student details below using dataframes:')
    print(dataframe_read_student)


# display_Student_data()


def sort_student_dataframe():
    df_student_info = pd.read_csv('students_file.csv')

    print("1 - To sort Student Information based on First Name")
    print("2 - To sort Student Information based on Last Name")
    print("3 - To sort Student Information based on Majors")
    print("4 - To sort Student Information based on Age")
    print("5 - To sort Student Information based on GPA")
    sort_condition = int(input("Enter the sort condition: "))

    if sort_condition == 1:
        print('sorted student data by First name')
        print(df_student_info.sort_values('FIRSTNAME'))

    elif sort_condition == 2:
        print('sorted student data by Last Name')
        print(df_student_info.sort_values('LASTNAME'))

    elif sort_condition == 3:
        print('sorted student data by Major')
        print(df_student_info.sort_values('MAJOR'))

    elif sort_condition == 4:
        print('sorted student data by Age')
        df_student_info['DOB'] = pd.to_datetime(df_student_info.DOB)
        print(df_student_info.sort_values(by=['DOB']))

    elif sort_condition == 5:
        print('sorted student data by GPA')
        print(df_student_info.sort_values('GPA'))

    else:
        print("Invalid input, enter a value between 1 and 5")


# sort_student_dataframe()


def search_student_dataframe():
    df_student_info = pd.read_csv('students_file.csv')

    print("1 - To search Student Information based on Student ID")
    print("2 - To search Student Information based on Last Name")
    print("3 - To search Student Information based Majors")

    search_condition = int(input("Enter the searching option: "))

    if search_condition == 1:
        search_STUDENTID = int(input('Enter searching Student ID: '))
        print(df_student_info.loc[df_student_info['STUDENTID'] == search_STUDENTID])

    elif search_condition == 2:
        search_LastName = input('Enter searching Last Name: ')
        print(df_student_info.loc[df_student_info['LASTNAME'].str.upper() == search_LastName.upper()])

    elif search_condition == 3:
        search_Major = input('Enter searching Majors: ')
        print(df_student_info.loc[df_student_info['MAJOR'].str.upper() == search_Major.upper()])
    else:
        print('Invalid Input, enter a value between 1 and 3')


# search_student_dataframe()


def modify_student_dataframe():
    df_student_info = pd.read_csv('students_file.csv')
    print("Displaying details of all Students: ")
    print(df_student_info)

    print("\nReplace data based on: ")
    print(" 1 - Student ID")
    print(" 2 - Student's First Name")
    print(" 3 - Student's Last Name")

    modify_search_condition = int(input("\nEnter the searching condition: "))
    modify_index = -1

    if modify_search_condition == 1:
        modify_Search_ID = int(input('Enter searching Student ID to modify details : '))
        print(df_student_info.loc[df_student_info['STUDENTID'] == modify_Search_ID])
        print(df_student_info.index[df_student_info['STUDENTID'] == modify_Search_ID].tolist())
        modify_index = (df_student_info.index[df_student_info['STUDENTID'] == modify_Search_ID].tolist())

    elif modify_search_condition == 2:
        modify_Search_First_Name = input('Enter searching Student First Name to modify details : ')
        print(df_student_info.loc[df_student_info['FIRSTNAME'] == modify_Search_First_Name])
        print(df_student_info.index[df_student_info['FIRSTNAME'] == modify_Search_First_Name].tolist())
        modify_index = (df_student_info.index[df_student_info['FIRSTNAME'] == modify_Search_First_Name].tolist())

    elif modify_search_condition == 3:
        modify_Search_LastName = input('Enter searching Last Name: ')
        print(df_student_info.loc[df_student_info['LASTNAME'] == modify_Search_LastName])
        print(df_student_info.index[df_student_info['LASTNAME'] == modify_Search_LastName].tolist())
        modify_index = (df_student_info.index[df_student_info['LASTNAME'] == modify_Search_LastName].tolist())
    else:
        print("Invalid input, enter a value between 1 and 3")

    if modify_index == -1:
        print('No results found..')

    else:
        field_to_modify = input('Enter the  filed to be modified: ').upper()
        new_value = input('Enter the  value to be updated: ')

        df_student_info.at[modify_index, field_to_modify] = new_value
        print(df_student_info)
        df_student_info.to_csv('students_file.csv', encoding='utf-8', index=False)


def main():
    student_details_header()

    while True:
        print("Menu Options: ")
        print("1 - To add a new Student data")
        print("2 - To display data of all Students")
        print("3 - To display sorted Student Information")
        print("4 - To search for specific Student Information")
        print("5 - To modify Student data")
        print("6 - To exit\n")

        try:
            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                student_data()

            elif user_choice == 2:
                display_Student_data()

            elif user_choice == 3:
                sort_student_dataframe()

            elif user_choice == 4:
                search_student_dataframe()

            elif user_choice == 5:
                modify_student_dataframe()

            elif user_choice == 6:
                break

            else:
                print("Invalid input, enter a value between 1 and 6")

        except ValueError:
            print('Invalid input, Try again!')


main()
