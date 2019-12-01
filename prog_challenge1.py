# The main module


def main():
    endProgram, totalScores, averageScores, score, number, counter = declaredVariables()

    while endProgram == "no":
        endProgram, totalScores, averageScores, score, number, counter = declaredVariables()

        number = getNumber()
        totalScores = getScores(totalScores, number)
        averageScores = getAverage(totalScores, number)
        printAverage(averageScores)
        endProgram = input("Do you want to end the program? (yes/no): ")


def declaredVariables():
    endProgram = "no"
    totalScores = 0.0
    counter = 0
    score = 0.0
    averageScores = 0.0
    number = 0
    return endProgram, totalScores, averageScores, score, number, counter


def getNumber():
    number = int(input("How many students took the test: "))
    return number


def getScores(totalScores, number):
    for counter in range(0, number):
        score = int(input("Enter score for the student: "))
        totalScores = totalScores + score
    return totalScores


def getAverage(totalScores, number):
    averageScores = totalScores / number
    return averageScores


def printAverage(averageScores):
    print("The average scores is ", float(averageScores))


main()
