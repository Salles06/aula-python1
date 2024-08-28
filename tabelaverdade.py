# Aulaquarta

a = 2
b = 6
c = 3

operacao1 = a == b and c * a == b
print (operacao1)
operacao1 = a == b or c * a == b
print (operacao1)

operacao2 = a > 5 or b > 3
print (operacao2)
operacao2 = a > 5 and b > 3
print (operacao2)

operacao3 = a < 5 or c >= 3
print (operacao3)
operacao3 = a < 5 and c >= 3
print (operacao3)

operacao4 = a == (c+b) and b == c
print(operacao4)
operacao4 = a == (c+b) or b == c
print(operacao4)

operacao5 = not b == 6 and 3*2 == b
print(operacao5)
operacao5 = not b == 6 or 3*2 == b
print(operacao5)

operacao6 = c < 5 and not b > 6
print(operacao6)
operacao6 = c < 5 or not b > 6
print(operacao6)
