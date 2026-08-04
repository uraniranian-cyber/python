def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number != 1:
        if is_even(number):
            number /= 2
            count += 1
        else:
            number = number * 3 + 1
            count += 1

    return count
