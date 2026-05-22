a = 10
b = 20
aux = a
a = b
b = aux
print(a, b)

a = 10
b = 20
a, b = b, a
print(a, b)