import math

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("На ноль делить нельзя.")
    return a / b

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2*a),
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

def geometric_sum(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)

def count_words(text):
    return len(text.split())

def find_substring(text, substring):
    return substring in text

def to_uppercase(text):
    return text.upper()

