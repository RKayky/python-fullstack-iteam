import json

funcionarios = [
    {"nome": "Ana", "cargo": "Desenvolvedora", "salario": 5000.0, "departamento": "TI"},
    {"nome": "Carlos", "cargo": "Analista", "salario": 4000.0, "departamento": "RH"},
    {"nome": "Maria", "cargo": "Gerente", "salario": 8000.0, "departamento": "Vendas"}
]

with open("funcionarios.json", "w") as f:
    json.dump(funcionarios, f, indent=4)

with open("funcionarios.json", "r") as f:
    dados = json.load(f)

print(f"{'Nome':<10} | {'Cargo':<15} | {'Salário':<10} | {'Departamento'}")
print("-" * 55)
total_salario = 0

for func in dados:
    print(f"{func['nome']:<10} | {func['cargo']:<15} | R${func['salario']:<8} | {func['departamento']}")
    total_salario += func['salario']

print(f"\nSalário Médio: R$ {total_salario / len(dados):.2f}")