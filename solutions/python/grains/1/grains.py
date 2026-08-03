holder = []
num = 1

for i in range(64):
    holder.append(num)
    num *= 2
    
    

def square(number):
    if number in range(1, 65):
        return holder[number - 1]
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    count = 0
    for i in holder:
        count += i
    return count
