def is_armstrong_number(number):
    if type(number) == str:
        holder = []
        count = 0
        for i in number:
            holder.append(int(i)**len(number))
        for j in holder:
            count += j
        if int(number) == count:
            return True
        else:
            return False
    if type(number) == int:
        digit = str(number)
        holder = []
        count = 0
        for i in digit:
            holder.append(int(i)**len(digit))
        for j in holder:
            count += j
        if int(digit) == count:
            return True
        else:
            return False