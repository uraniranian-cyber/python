def score(x, y):
    d = (x ** 2 + y ** 2) ** 0.5
    score = 0
    if d <= 1:
        score = 10
    elif d <= 5:
        score = 5
    elif d <= 10:
        score = 1
    return score
