# Exercice 6 — Lambda et closure

# Lambda
addition = lambda a, b: a + b
print("Addition :", addition(5, 3))

# Closure
def multiplicateur(x):
    def multiplier(y):
        return x * y
    return multiplier

double = multiplicateur(2)
triple = multiplicateur(3)

print("Double de 5 :", double(5))
print("Triple de 5 :", triple(5))
