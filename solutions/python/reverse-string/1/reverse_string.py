def reverse(text):
    length = len(text)
    holder = []
    for i in range(length):
        holder.append(text[length - i - 1])

    return ''.join(holder)