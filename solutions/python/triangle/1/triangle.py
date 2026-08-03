def is_triangle(a, b, c):
    return (
        a > 0 and b > 0 and c > 0
        and a + b >= c
        and a + c >= b
        and b + c >= a
    )
def equilateral(sides):
    a,b,c = sides[0],sides[1],sides[2]
    if is_triangle(a, b, c):
        if a == b == c:
            return True
        else:
            return False
    else:
        return False

def isosceles(sides):
    a,b,c = sides[0],sides[1],sides[2]
    if is_triangle(a, b, c):
        if (
            a == b or
            a == c or
            b == c
        ):
            return True
        else:
            return False
    else:
        return False

def scalene(sides):
    a,b,c = sides[0],sides[1],sides[2]
    if is_triangle(a, b, c):
        if (
            a != b and
            a != c and
            b != c
        ):
            return True
        else:
            return False
    else:
        return False 
