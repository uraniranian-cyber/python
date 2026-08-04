def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if type(number) is not int or number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    holder = []
    count = 0
    for i in range(1, number):
        if number % i == 0:
            holder.append(i)
    for j in holder:
        count += j
    
    if number == count:
        return "perfect"
    elif number < count:
        return "abundant"
    elif number > count:
        return "deficient"
    
