num1 = int(input("Qual é o primeiro número? "))
num2 = int(input("Qual é o segundo número? "))

print("\n--- Resultados ---")
print(f"O primeiro número é maior que o segundo? {num1 > num2}")
print(f"Os dois são iguais? {num1 == num2}")
print(f"Ambos são positivos? {num1 > 0 and num2 > 0}")
print(f"Pelo menos um é maior que 100? {num1 > 100 or num2 > 100}")
print(f"O primeiro é diferente de zero? {num1 != 0}")