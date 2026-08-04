def convert(number):
    holder = []
    if number % 3 == 0:
        holder.append("Pling")
    if number % 5 == 0:
        holder.append("Plang")
    if number % 7 == 0:
        holder.append("Plong")
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0 :
        holder.append(str(number))
    res = ""
    for i in holder:
        res += i
    return res