def find_average(numbers: "list[int]") -> float:
    ## raise NotImplementedError
    sum = 0
    for number in numbers:
        sum = sum + number

    return sum / len(numbers)

