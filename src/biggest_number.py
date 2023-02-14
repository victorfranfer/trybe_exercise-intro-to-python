# 1- Create a function that receives two numbers and returns the biggest of them

def find_biggest_number(first_number: int, second_number: int) -> int:
    ## raise NotImplementedError
    if first_number >= second_number:
        return first_number
    else:
        return second_number

