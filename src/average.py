# 2- Create a function that returns the average of a list of numbers

def find_average(numbers: "list[int]") -> float:
    sum = 0
    for number in numbers:
        sum = sum + number

    return sum / len(numbers)
