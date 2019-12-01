# # import random
# #
# # print(random.randint(1,100))
# #
# #
#
# # inputDate = input("Enter the date in format 'dd/mm/yy' : ")
#
#
# class DateOfBirth:
#     def __init__(self, user_input_date):
#         self.inputDate = user_input_date
#         import datetime
#
#         day, month, year = self.inputDate.split('/')
#
#         isValidDate = True
#         try:
#             datetime.datetime(int(year), int(month), int(day))
#         except ValueError:
#             isValidDate = False
#
#         if not isValidDate:
#             print("Input date is not valid..")
#
#         # pass
#
#     # import datetime
#
#     # inputDate = input("Enter the date in format 'dd/mm/yy' : ")
#
#     # day, month, year = inputDate.split('/')
#     #
#     isValidDate = True
#     try:
#         datetime.datetime(int(year), int(month), int(day))
#     except ValueError:
#         isValidDate = False
#
#     if isValidDate:
#         print("Input date is valid ..")
#     else:
#         print("Input date is not valid..")
#
#
# '''
# import datetime
#
# inputDate = input("Enter the date in format 'dd/mm/yy' : ")
#
# day,month,year = inputDate.split('/')
#
# isValidDate = True
# try :
#     datetime.datetime(int(year),int(month),int(day))
# except ValueError :
#     isValidDate = False
#
# if(isValidDate) :
#     print ("Input date is valid ..")
# else :
#     print ("Input date is not valid..")     '''


isValidDate = True
while isValidDate:
    DOB = input("Enter Student's Date of Birth in 'dd/mm/yyyy' format: ")
    import datetime

    day, month, year = DOB.split('/')
    isValidDate = False
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        print("Input date is Invalid..Try again")
        isValidDate = True
        print("VAlid-", isValidDate)
