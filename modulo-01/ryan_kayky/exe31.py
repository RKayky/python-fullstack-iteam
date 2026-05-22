import json

cadastro = {"id": 1042, "nome": "Fernanda Costa", "email": "fernanda@empresa.com"}
perfil   = {"id": 1042, "cargo": "Engenheira de Software", "nivel": "Senior",
            "salario": 12500.00, "habilidades": ["Python", "Django", "PostgreSQL"]}

funcionario_completo = {**cadastro, **perfil}

with open("funcionario_completo.json", "w") as f:
    json.dump(funcionario_completo, f, indent=4)

with open("funcionario_completo.json", "r") as f:
    func = json.load(f)

print(f"Nome: {func['nome']} ({func['cargo']})")
print("Habilidades:")
for i, hab in enumerate(func['habilidades'], start=1):
    print(f"{i}. {hab}")