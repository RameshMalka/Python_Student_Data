# Lab6-3, Practicing For loops
# the main function


def main():
    print('I will display the numbers 1 through 5.')
    # A Basic For loop
    for num in [1, 2, 3, 4, 5]:
        print(num)

    print('I will display the numbers 1 through 60.')
    # The Second Counter code
    for num in range(1, 61):
        print(num)

    # The Accumulator code
    total = 0
    for i in range(5):
        number = int(input("Enter a number: "))
        total = total + number
    print("The total is ", total)

    # The Average Age code
    totalAge = 0
    averageAge = 0
    number = int(input("How many ages do you want to enter: "))
    for counter in range(0, number):
        age = int(input("Enter an age: "))
        totalAge = totalAge + age
    averageAge = totalAge / number
    print("The average age is ", averageAge)


# calls main
main()
