def forma_triangulo(a: int, b: int, c: int) -> bool:
        return abs(b - c) < a < (b + c) or abs(a - c) < b < (a + c) or abs(a - b) < c < (a + b)
    
print(forma_triangulo(3, 4, 5))
print(forma_triangulo(1, 2, 3))