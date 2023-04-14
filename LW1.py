import math

def equation_sovle(a, b, c):

    if a == b == c == 0:
        return math.inf
    if a == b == 0 and c != 0:
        return None
    if a == 0:
        return [-c/b]

    disc = b*b - 4*a*c
    lfRoot = -b/(2*a) + math.sqrt(abs(disc))/(2*a)
    rtRoot = -b/(2*a) - math.sqrt(abs(disc))/(2*a)

    if disc > 0:
        return [lfRoot, rtRoot]
    elif disc == 0:
        return [lfRoot]
    else:
        return None

def fibonacci(i):
    
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)

def Hanoi(n, start, finish):
    
    if n <= 0:
        return
    
    temp = 6 - start - finish
    Hanoi(n-1, start, temp)
    print("Move disk", n, "from", start, "to", finish)
    Hanoi(n-1, temp, finish)

Hanoi(4, 1, 3)